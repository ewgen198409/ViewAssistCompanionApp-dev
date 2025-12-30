""Config flow for View Assist Companion App integration."""
import logging
from typing import Any, Dict, Optional

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_entry_oauth2_flow

from .const import (
    DOMAIN,
    DEFAULT_HA_PORT,
    DEFAULT_HA_URL,
    DEFAULT_DASHBOARD,
    DEFAULT_WAKE_WORD,
    DEFAULT_WAKE_WORD_SOUND,
    DEFAULT_WAKE_WORD_THRESHOLD,
    DEFAULT_CONTINUE_CONVERSATION,
    DEFAULT_NOTIFICATION_VOLUME,
    DEFAULT_MUSIC_VOLUME,
    DEFAULT_DUCKING_VOLUME,
    DEFAULT_MIC_GAIN,
    DEFAULT_SCREEN_BRIGHTNESS,
    DEFAULT_SCREEN_AUTO_BRIGHTNESS,
    DEFAULT_SWIPE_REFRESH,
    DEFAULT_SCREEN_ALWAYS_ON,
    DEFAULT_DO_NOT_DISTURB,
    DEFAULT_DARK_MODE,
    DEFAULT_DIAGNOSTICS_ENABLED,
    DEFAULT_ZOOM_LEVEL,
    DEFAULT_SCREEN_ON_WAKE_WORD,
    DEFAULT_SCREEN_ON_BUMP,
    DEFAULT_SCREEN_ON_PROXIMITY,
    DEFAULT_SCREEN_ON_MOTION,
    DEFAULT_ENABLE_NETWORK_RECOVERY,
    DEFAULT_ENABLE_MOTION_DETECTION,
    DEFAULT_MOTION_DETECTION_SENSITIVITY,
    DEFAULT_SCREEN_TIMEOUT,
    DEFAULT_HOME_URL,
    DEFAULT_AUTO_REDIRECT_TIME,
)

_LOGGER = logging.getLogger(__name__)

class VACAConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for View Assist Companion App."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None) -> FlowResult:
        """Handle the initial step."""
        return self.async_create_entry(
            title="View Assist Companion App",
            data={},
        )

class VAOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for View Assist Companion App."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input: Optional[Dict[str, Any]] = None) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema(
            {
                vol.Optional(
                    "ha_port",
                    default=self.config_entry.options.get("ha_port", DEFAULT_HA_PORT),
                ): int,
                vol.Optional(
                    "ha_url",
                    default=self.config_entry.options.get("ha_url", DEFAULT_HA_URL),
                ): str,
                vol.Optional(
                    "ha_dashboard",
                    default=self.config_entry.options.get("ha_dashboard", DEFAULT_DASHBOARD),
                ): str,
                vol.Optional(
                    "wake_word",
                    default=self.config_entry.options.get("wake_word", DEFAULT_WAKE_WORD),
                ): vol.In(["alexa", "hey_jarvis", "hey_mycroft", "hey_raspy", "ok_nabu", "ok_computer"]),
                vol.Optional(
                    "wake_word_sound",
                    default=self.config_entry.options.get("wake_word_sound", DEFAULT_WAKE_WORD_SOUND),
                ): vol.In(["none", "alexa"]),
                vol.Optional(
                    "wake_word_threshold",
                    default=self.config_entry.options.get("wake_word_threshold", DEFAULT_WAKE_WORD_THRESHOLD),
                ): vol.All(vol.Coerce(int), vol.Range(min=1, max=10)),
                vol.Optional(
                    "continue_conversation",
                    default=self.config_entry.options.get("continue_conversation", DEFAULT_CONTINUE_CONVERSATION),
                ): bool,
                vol.Optional(
                    "notification_volume",
                    default=self.config_entry.options.get("notification_volume", DEFAULT_NOTIFICATION_VOLUME),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=100)),
                vol.Optional(
                    "music_volume",
                    default=self.config_entry.options.get("music_volume", DEFAULT_MUSIC_VOLUME),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=100)),
                vol.Optional(
                    "ducking_volume",
                    default=self.config_entry.options.get("ducking_volume", DEFAULT_DUCKING_VOLUME),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=100)),
                vol.Optional(
                    "mic_gain",
                    default=self.config_entry.options.get("mic_gain", DEFAULT_MIC_GAIN),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=20)),
                vol.Optional(
                    "screen_brightness",
                    default=self.config_entry.options.get("screen_brightness", DEFAULT_SCREEN_BRIGHTNESS),
                ): vol.All(vol.Coerce(int), vol.Range(min=1, max=100)),
                vol.Optional(
                    "screen_auto_brightness",
                    default=self.config_entry.options.get("screen_auto_brightness", DEFAULT_SCREEN_AUTO_BRIGHTNESS),
                ): bool,
                vol.Optional(
                    "swipe_refresh",
                    default=self.config_entry.options.get("swipe_refresh", DEFAULT_SWIPE_REFRESH),
                ): bool,
                vol.Optional(
                    "screen_always_on",
                    default=self.config_entry.options.get("screen_always_on", DEFAULT_SCREEN_ALWAYS_ON),
                ): bool,
                vol.Optional(
                    "do_not_disturb",
                    default=self.config_entry.options.get("do_not_disturb", DEFAULT_DO_NOT_DISTURB),
                ): bool,
                vol.Optional(
                    "dark_mode",
                    default=self.config_entry.options.get("dark_mode", DEFAULT_DARK_MODE),
                ): bool,
                vol.Optional(
                    "diagnostics_enabled",
                    default=self.config_entry.options.get("diagnostics_enabled", DEFAULT_DIAGNOSTICS_ENABLED),
                ): bool,
                vol.Optional(
                    "zoom_level",
                    default=self.config_entry.options.get("zoom_level", DEFAULT_ZOOM_LEVEL),
                ): vol.All(vol.Coerce(int), vol.Range(min=-5, max=5)),
                vol.Optional(
                    "screen_on_wake_word",
                    default=self.config_entry.options.get("screen_on_wake_word", DEFAULT_SCREEN_ON_WAKE_WORD),
                ): bool,
                vol.Optional(
                    "screen_on_bump",
                    default=self.config_entry.options.get("screen_on_bump", DEFAULT_SCREEN_ON_BUMP),
                ): bool,
                vol.Optional(
                    "screen_on_proximity",
                    default=self.config_entry.options.get("screen_on_proximity", DEFAULT_SCREEN_ON_PROXIMITY),
                ): bool,
                vol.Optional(
                    "screen_on_motion",
                    default=self.config_entry.options.get("screen_on_motion", DEFAULT_SCREEN_ON_MOTION),
                ): bool,
                vol.Optional(
                    "enable_network_recovery",
                    default=self.config_entry.options.get("enable_network_recovery", DEFAULT_ENABLE_NETWORK_RECOVERY),
                ): bool,
                vol.Optional(
                    "enable_motion_detection",
                    default=self.config_entry.options.get("enable_motion_detection", DEFAULT_ENABLE_MOTION_DETECTION),
                ): bool,
                vol.Optional(
                    "motion_detection_sensitivity",
                    default=self.config_entry.options.get("motion_detection_sensitivity", DEFAULT_MOTION_DETECTION_SENSITIVITY),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=100)),
                vol.Optional(
                    "screen_timeout",
                    default=self.config_entry.options.get("screen_timeout", DEFAULT_SCREEN_TIMEOUT),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=300)),
                vol.Optional(
                    "home_url",
                    default=self.config_entry.options.get("home_url", DEFAULT_HOME_URL),
                ): str,
                vol.Optional(
                    "auto_redirect_time",
                    default=self.config_entry.options.get("auto_redirect_time", DEFAULT_AUTO_REDIRECT_TIME),
                ): vol.All(vol.Coerce(int), vol.Range(min=0, max=3600)),
            }
        )

        return self.async_show_form(step_id="init", data_schema=schema)
