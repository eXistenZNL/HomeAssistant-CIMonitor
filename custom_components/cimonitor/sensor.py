import logging
import socketio

from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)
DOMAIN = "cimonitor"

async def async_setup_platform(hass, config, async_add_entities, discovery_info = None):
    sensor = SocketIOStatusSensor()
    async_add_entities([sensor])

    socketio_url = hass.data[DOMAIN]['socketio_url']

    client = socketio.AsyncClient()

    @client.on("global-state-change")
    async def on_status_state_change(status):
        try:
            _LOGGER.debug("Received event 'status-state-change' with data: %s", status)
            if isinstance(status, str):
                _LOGGER.info("Status received: %s", status)
                sensor.update_status(status)
            else:
                _LOGGER.warning("Received non-string data for 'global-state-change': %s", status)
        except Exception as e:
            _LOGGER.error("Error handling 'global-state-change' event: %s", e)

    async def connect_socket(_socketio_url):
        try:
            await client.connect(_socketio_url)
            _LOGGER.info("Connected to Socket.IO server at %s", _socketio_url)
        except Exception as e:
            _LOGGER.error("Failed to connect to Socket.IO server: %s", e)

    async def disconnect_socket():
        await client.disconnect()
        _LOGGER.info("Disconnected from Socket.IO server")

    await connect_socket(socketio_url)
    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, disconnect_socket)


class SocketIOStatusSensor(Entity):

    def __init__(self):
        self._status = None

    @property
    def name(self):
        return "CIMonitor"

    @property
    def state(self):
        return self._status

    def update_status(self, status):
        self._status = status
        self.async_write_ha_state()
