```markdown
# DialogStream Python Package

This repository contains the Python package for DialogStream, a powerful and flexible conversational AI platform.

## Installation

To install the DialogStream Python package, you can use pip:

```bash
pip install dialogstream
```

## Usage

Here's a basic example of how to use the DialogStream package:

### Konfiguracja przepływów (flows.json)
Plik `config/flows.json` definiuje przepływy strumieni wideo:
```json
{
  "flows": [
    {
      "name": "RTSP z detekcją ruchu",
      "steps": [
        "rtsp://user:pass@camera:554/stream",
        "process://motion?fps=5&threshold=0.3",
        "file:///recordings/stream1.mp4"
      ]
    },
    {
      "name": "RTSP z zapisem czasowym", 
      "steps": [
        "rtsp://user:pass@camera:554/stream",
        "file:///recordings/%Y%m%d_%H%M.mp4"
      ]
    }
  ]
}
```

Każdy przepływ zawiera:
- `name`: Nazwa opisowa przepływu
- `steps`: Lista kroków przetwarzania, gdzie każdy krok to URL w formacie:
    - `rtsp://` - źródło RTSP
    - `process://` - proces przetwarzania z parametrami
    - `file://` - zapis do pliku (wspiera strftime format)

### Konfiguracja procesów (process.json)
Plik `config/process.json` definiuje reguły przetwarzania:
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

Każda reguła zawiera:
- `filter`: Lista wzorców URL do dopasowania
- `run`: Lista poleceń shell do wykonania, gdzie:
    - `$1, $2, $3...` - odnoszą się do kolejnych URL-i z sekcji filter
    - Polecenia są wykonywane w kolejności zdefiniowanej w liście


For more detailed information, please refer to the [official documentation](https://github.com/dialogstream-com/python/tree/main/docs).

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/dialogstream-com/python/blob/main/LICENSE) file for details.
```

This README file provides a high-level overview of the DialogStream Python package, including installation instructions, usage examples, and links to the official documentation, contributing guidelines, and license information.