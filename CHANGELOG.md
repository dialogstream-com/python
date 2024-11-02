# Changelog
## [1.4.8] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji, logo

## [1.4.7] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji, logo

## [1.4.6] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji, logo

## [1.4.5] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji, logo

## [1.4.4] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji

## [1.4.3] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji

## [1.4.2] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji

## [1.4.1] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji i opisu licencji

## [1.3.12] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji

## [1.3.11] - 2024-11-02

### Zmieniono
- Poprawiono ścieżki konfiguracyjne w test.py:
  - Zaktualizowano domyślne ścieżki do plików konfiguracyjnych
  - Dodano obsługę ścieżek względnych dla dialogstream/config/
- Ulepszono zarządzanie procesami:
  - Dodano automatyczne tworzenie katalogów dla wyjść (motion, timelapses)
  - Poprawiono obsługę błędów przy tworzeniu plików wyjściowych
  - Ulepszono logowanie błędów procesów ffmpeg

## [1.3.10] - 2024-11-02

### Zmieniono
- aktualizacja dokumentacji
  
## [1.3.9] - 2024-11-02

### Dodano
- Nowe pliki konfiguracyjne w katalogu config/:
  - schedule.json do planowania zadań:
    - Wsparcie dla wyrażeń cron
    - Automatyczne tworzenie timelapse
    - Harmonogram backupów i archiwizacji
    - Automatyczne czyszczenie starych plików
  - reactions.json do obsługi zdarzeń:
    - Reakcje na wykrycie ruchu
    - Automatyczne nagrywanie po wykryciu ruchu
    - Zarządzanie przestrzenią dyskową
    - Backup przy stabilnym połączeniu

## [1.3.8] - 2024-11-02

### Zmieniono
- Ujednolicono format nazw plików w procesach file://:
  - Dodano automatyczne parsowanie wzorców daty (%Y%m%d-%H%M%S)
  - Zaktualizowano wszystkie procesy do używania strftime
  - Format nazw plików: YYYYMMDD-HHMMSS.{mp4|jpg}

## [1.3.7] - 2024-11-02

### Dodano
- Rozszerzono konfigurację procesów w process.json:
  - Dodano opisy (description) do wszystkich procesów wyjaśniające ich funkcje
  - Dodano nowy proces do zapisywania klatek JPEG przy wykryciu ruchu:
    - Zapis do katalogu frames
    - Automatyczne timestampy w nazwach plików
    - Konfiguracja FPS dla przechwytywania klatek

## [1.3.6] - 2024-11-02

### Dodano
- Wykrywanie istniejących procesów przy starcie:
  - Sprawdzanie procesów z pliku konfiguracyjnego
  - Wyświetlanie szczegółowych informacji o procesach
  - Monitorowanie użycia CPU i pamięci
  - Śledzenie czasu startu i działania procesów

### Zmieniono
- Ulepszono zarządzanie procesami:
  - Dodano nową klasę ManagedProcess
  - Dodano narzędzia do monitorowania procesów
  - Ulepszono formatowanie informacji o procesach
  - Dodano szczegółowe logowanie stanu procesów

## [1.3.5] - 2024-11-02

### Poprawiono
- Naprawiono błąd tworzenia procesów:
  - Usunięto konflikt między preexec_fn i start_new_session
  - Uproszczono zarządzanie grupami procesów
  - Poprawiono mechanizm zamykania procesów potomnych

## [1.3.4] - 2024-11-02

### Poprawiono
- Ulepszono mechanizm zamykania aplikacji:
  - Dodano blokadę przed wielokrotnym wywołaniem stop()
  - Dodano rekursywne zabijanie drzewa procesów
  - Ulepszono izolację procesów przez start_new_session
  - Wymuszenie zakończenia aplikacji przez sys.exit(0)
  - Poprawiono obsługę sygnałów w głównej pętli
  - Dodano zabezpieczenie przed zombie-procesami

## [1.3.3] - 2024-11-02

### Dodano
- Ulepszone zarządzanie procesami i bezpieczne zamykanie:
  - Obsługa sygnałów SIGTERM i SIGINT
  - Graceful shutdown z timeoutem dla segmentów
  - Grupowanie procesów (process groups)
  - Kolejkowanie procesów
- Zabezpieczenia przed uszkodzeniem plików wideo:
  - Dokumentacja segmentacji ffmpeg
  - Przykłady konfiguracji z timestampami
  - Automatyczna rotacja plików

### Zmieniono
- Przepisano logikę zamykania aplikacji:
  - Dodano event shutdown
  - Ulepszono obsługę wątków (daemon threads)
  - Dodano timeout dla zamykania procesów
  - Poprawiono cleanup zasobów

## [1.3.2] - 2024-11-02

### Zmieniono
- Zaktualizowano dokumentację formatów konfiguracyjnych:
  - Dodano szczegółowy opis formatu flows.json
  - Dodano szczegółowy opis formatu process.json
  - Zastąpiono przykłady YAML poprawnymi przykładami JSON
  - Dodano dokumentację parametrów URL i zmiennych w komendach

## [1.3.1] - 2024-11-02

### Zmieniono
- Przepisano logikę dopasowywania URL-i:
  - Dodano normalizację łańcuchów strumieni
  - Ulepszono parsowanie URL-i process://
  - Poprawiono obsługę schematów URL
  - Dodano lepszą obsługę tablic w konfiguracji

### Poprawiono
- Naprawiono błędy w dopasowywaniu procesów do strumieni
- Ulepszono analizę ścieżek URL
- Poprawiono obsługę parametrów zapytań

## [1.3.0] - 2024-11-02

### Dodano
- Ulepszone dopasowywanie filtrów:
  - Obsługa parametrów zapytań w URL-ach process://
  - Wsparcie dla wielu wyjść w łańcuchu strumieni
  - Elastyczne dopasowywanie schematów URL

### Poprawiono
- Naprawiono błędy w dopasowywaniu procesów do strumieni
- Zaktualizowano obsługę list w łańcuchach strumieni
- Poprawiono podstawianie zmiennych w komendach

## [1.2.0] - 2024-11-02

### Dodano
- Argumenty wiersza poleceń dla plików konfiguracyjnych:
  - `--stream-config` / `-s`: Ścieżka do pliku konfiguracji strumieni
  - `--process-config` / `-p`: Ścieżka do pliku konfiguracji procesów
  - Domyślne wartości pozostają jako `config/stream.yaml` i `config/process.yaml`

## [1.1.0] - 2024-11-02

### Dodano
- Wsparcie dla debugowania w kontenerach Docker:
  - Dodano debugpy w kontenerze sfr-main
  - Skonfigurowano porty debugowania (5678, 5679)
- Dodano brakujące zależności w kontenerach:
  - psutil dla monitorowania metryk
  - debugpy dla wsparcia debugowania

### Zmieniono
- Zaktualizowano dokumentację Docker:
  - Dodano instrukcje instalacji i uruchomienia
  - Opisano konfigurację kontenerów
  - Dodano informacje o portach i wolumenach
  - Dodano instrukcje debugowania

## [1.0.0] - 2024-11-02

### Dodano
- Prefix "SFR" do logów dla lepszej identyfikacji w formacie `[SFR]`
- Kolorowe formatowanie logów przy użyciu `colorlog>=6.7.0`
- Szczegółowe informacje o stanie systemu podczas inicjalizacji:
  - Status tworzenia katalogów
  - Weryfikacja zależności systemowych
  - Status instalacji wymagań Python
  - Informacje o konfiguracji systemd

### Zmieniono
- Ulepszono formatowanie komunikatów logowania:
  - DEBUG: kolor cyjan
  - INFO: kolor zielony
  - WARNING: żółty
  - ERROR: czerwony
  - CRITICAL: czerwony tekst na białym tle
- Rozszerzono dokumentację klas i metod w kodzie źródłowym
- Zaktualizowano zależności projektu:
  - pyyaml>=6.0
  - python-dotenv>=0.19.0
  - ffmpeg-python>=0.2.0
  - typing-extensions>=4.0.0
  - colorlog>=6.7.0
  - click>=8.0.0
