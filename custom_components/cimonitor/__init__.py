import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)
DOMAIN = "cimonitor"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:

    socketio_url = config[DOMAIN].get('socketio_url')

    if not socketio_url:
        _LOGGER.error("Socket.IO URL must be set in the YAML config")
        return False

    hass.data[DOMAIN] = {
        'socketio_url': socketio_url
    }

    await async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True
