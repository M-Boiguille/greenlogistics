"""Client LLM abstrait pour Deepseek (et futurs providers)."""

import hashlib
import json
import os
from dataclasses import dataclass
from typing import Any, Protocol

import requests

from .cache import Cache


class LLMClient(Protocol):
    """Interface commune pour tous les providers LLM."""

    def chat(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        json_mode: bool = False,
    ) -> str:
        """Envoie une conversation et retourne le contenu texte de la réponse."""
        ...


@dataclass
class DeepseekClient:
    """Client pour l'API Deepseek."""

    api_key: str
    model: str = "deepseek-reasoner"
    cache: Cache | None = None

    def _cache_key(
        self,
        messages: list[dict[str, str]],
        temperature: float,
        json_mode: bool,
    ) -> str:
        payload = json.dumps(
            {
                "messages": messages,
                "temperature": temperature,
                "json_mode": json_mode,
            },
            sort_keys=True,
        )
        return hashlib.sha256(payload.encode()).hexdigest()

    def chat(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        json_mode: bool = False,
    ) -> str:
        if self.cache:
            key = self._cache_key(messages, temperature, json_mode)
            cached = self.cache.get(key)
            if cached is not None:
                return cached

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}

        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        data: dict[str, Any] = response.json()
        content = str(data["choices"][0]["message"]["content"])

        if self.cache:
            self.cache.set(key, content)

        return content


def load_llm_from_env(cache: Cache | None = None) -> LLMClient:
    """Charge le provider LLM depuis les variables d'environnement."""
    provider = os.environ.get("LLM_PROVIDER", "deepseek").lower()
    if provider == "deepseek":
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY non défini")
        return DeepseekClient(api_key=api_key, cache=cache)
    raise ValueError(f"Provider LLM non supporté : {provider}")
