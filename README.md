# DialogStream Python Package

This repository contains the Python package for DialogStream, a powerful and flexible conversational AI platform.

## Installation

To install the DialogStream Python package, you can use pip:

```bash
pip install dialogstream
```

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate && pip install dialogstream
```
JSON
```bash
python router.py -s "config/stream.json" -p "config/process.json"
```


## Video stream testing

```bash
ffplay rtsp://192.168.1.2:554/Preview_01_sub
```

```bash
ffmpeg -i rtsp://192.168.1.2:554/Preview_01_sub -c copy -f segment -segment_time 6 -segment_format mp4 -strftime 1 -reset_timestamps 1 "./recordings/%Y%m%d_%H.mp4" -v debug
```



## Usage

Here's a basic example of how to use the DialogStream package:

![img.png](img.png)

### Flow configuration (flows.json)
The `config/flows.json` file defines video stream flows:
```json
{
  "flows": [
    {
      "name": "RTSP z detekcją ruchu i zapisaniem obrazów",
      "steps": [
        "rtsp://test1234:test1234@192.168.188.225:554/Preview_01_sub",
        "file:///motion"
      ]
    },
    {
      "name": "Timelapse z obrazów",
      "steps": [
        "file:///motion",
        "file:///timelapses"
      ]
    },
    {
      "name": "Timelapse z obrazów co 1 godzine",
      "steps": [
        "file:///motion",
        "schedule://0 */1 * * *",
        "file:///timelapses"
      ]
    },
    {
      "name": "Timelapse z obrazów co 1 godzine",
      "steps": [
        "file:///motion",
        "schedule://0 */1 * * *",
        "file:///timelapses"
      ]
    },
    {
      "name": "Email z powiadamieniem, gdy pojawi się nowy obiekt",
      "steps": [
        "subscribe://object_detected",
        "email:///info@softreck.dev"
      ]
    },
    {
      "name": "Wysyłanie powiadomienia, gdy pojawi się nowy obiekt",
      "steps": [
        "file:///motion",
        "process://detect_object_on_picture",
        "publish://object_detected"
      ]
    }
  ]
}
```

Each flow contains:
- `name`: A descriptive name for the flow
- `steps`: A list of processing steps, where each step is a URL in the format:
    - `rtsp://` - RTSP source
    - `process://` - Processing step with parameters
    - `file://` - Save to file (supports strftime format)

### Process configuration (process.json)
The `config/process.json` file defines processing rules:
```json
[
  {
    "filter": [
      "rtsp",
      "process://motion",
      "file"
    ],
    "run": [
      "shell://ffmpeg -i $1 -c copy -f segment -segment_time 6 -segment_format mp4 -strftime 1 -reset_timestamps 1 $3"
    ]
  },
  {
    "filter": [
      "rtsp",
      "file"
    ],
    "run": [
      "shell://ffmpeg -i $1 -c copy -f segment -segment_time 6 -segment_format mp4 -strftime 1 -reset_timestamps 1 $2"
    ]
  }
]
```

Each rule contains:
- `filter`: A list of URL patterns to match
- `run`: A list of shell commands to execute, where:
    - `$1, $2, $3...` - refer to the corresponding URLs from the filter section
    - Commands are executed in the order defined in the list




For more detailed information, please refer to the [official documentation](https://github.com/dialogstream-com/python/tree/main/docs).

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/dialogstream-com/python/blob/main/LICENSE) file for details.