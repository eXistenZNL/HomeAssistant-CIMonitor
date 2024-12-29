# CIMonitor integration for Home Assistant

[![License](https://img.shields.io/github/license/existenznl/homeassistant-cimonitor.svg?style=flat-square)](https://github.com/eXistenZNL/HomeAssistant-CIMonitor/blob/master/LICENSE) [![Sponsors](https://img.shields.io/github/sponsors/eXistenZNL?color=hotpink&style=flat-square)](https://github.com/sponsors/eXistenZNL)

## About

An integration for Home Assistant that makes the status of [CIMonitor](https://github.com/futureportal/cimonitor) available as a sensor.

## Why?

I sometimes want to open [CIMonitor](https://github.com/futureportal/cimonitor) in my TV, however I had no way of controlling the Philips Hue lights behind my TV.
This integration solves that, so I can easily control the Hue lights from Home Assistant based on the sensor status.

## How can I use it?

1. Add the following to your `configuration.yaml`:
    ```yaml
     cimonitor:
        socketio_url: wss://my.cimonitor.com
    ```
2. Add this repository as custom repository via HACS, and install the integration.
3. Restart your Home Assistant and you should have a sensor named `sensor.cimonitor` now.

## Bugs, questions, and improvements

If you found a bug or have a question, please open an issue on the GitHub Issue tracker.
Improvements can be sent by a Pull Request against the master branch and are greatly appreciated!

## Contributors

Thanks to [Rick van der Staaij](https://github.com/rick-nu) for creating [CIMonitor](https://github.com/futureportal/cimonitor), and to everyone else for helping out with this project!

[![Contributor avatars](https://contrib.rocks/image?repo=eXistenZNL/HomeAssistant-CIMonitor)](https://github.com/eXistenZNL/HomeAssistant-CIMonitor/graphs/contributors)
