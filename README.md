# View Assist Companion Android App

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/msp1974/ViewAssist_Companion_App/actions)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android-green.svg)](https://developer.android.com)

Автор приложения https://github.com/msp1974/ViewAssistCompanionApp/tree/dev

**View Assist Companion** - это Android-приложение, которое превращает ваше Android-устройство в умный голосовой помощник для Home Assistant. Приложение работает как Wyoming satellite, обеспечивая локальное распознавание голосовых команд без использования облачных сервисов Google.

## ✨ Особенности

- 🔊 **Локальное распознавание голоса** - работает без интернета и облачных сервисов
- 🎯 **Wake Word Detection** - активация по ключевым словам (hey_jarvis, ок_computer и др.)
- 🏠 **Интеграция с Home Assistant** - через Wyoming protocol
- 📱 **Управление экраном** - автоматическое включение/выключение экрана
- 🔒 **Автономность** - не зависит от Google Play Services и Firebase
- 🔐 **Автоматическая подпись** - встроенная система подписи APK для релизов
- 📷 **Распознавание движения** - опциональная камера для обнаружения движения
- 🔔 **Уведомления** - будильник и звуковые оповещения

## 🚀 Установка

### Из APK
1. Скачайте последнюю версию APK из [Releases](https://github.com/msp1974/ViewAssist_Companion_App/releases)
2. Установите APK на ваше Android-устройство
3. Предоставьте необходимые разрешения (микрофон, камера, уведомления)

### Из исходного кода
```bash
# Клонировать репозиторий
git clone https://github.com/msp1974/ViewAssist_Companion_App.git
cd ViewAssist_Companion_App

# Собрать релизную версию
./gradlew assembleRelease
```

## ⚙️ Настройка

### Home Assistant
1. Установите Wyoming integration в Home Assistant
2. Настройте satellite с указанием IP-адреса Android-устройства
3. Выберите wake word из доступных вариантов

### Приложение
1. Запустите приложение
2. Предоставьте разрешения на микрофон и камеру
3. Подключитесь к сети с Home Assistant
4. Приложение автоматически обнаружится как Wyoming satellite

## 🔧 Требования

- **Android**: 8.0 (API 26) или выше
- **Home Assistant**: с Wyoming integration
- **Свободное место**: ~100MB для моделей распознавания речи

## 🏗️ Архитектура

```
📱 View Assist Companion App
├── 🎤 Audio Processing (OpenWakeWord)
├── 🌐 Wyoming Protocol Server
├── 📱 Android System Integration
│   ├── 📱 Screen Control
│   ├── 🔊 Audio Management
│   ├── 📷 Camera (Motion Detection)
│   └── 🔒 Permissions
└── 🏠 Home Assistant Integration
```

## 🔑 Wake Words

Поддерживаемые ключевые слова для активации:
- hey_jarvis
- ок_computer
- hey_mycroft
- hey_rhasspy
- ok_nabu
- alexa

## 🔒 Конфиденциальность

- Все обработка голоса происходит локально на устройстве
- Нет передачи данных в облако
- Не требуется учетная запись Google
- Полностью автономная работа

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта!

### Как внести вклад:
1. Fork репозиторий
2. Создайте feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в branch (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

### Требования к коду:
- Kotlin style guide compliance
- Unit tests для новых функций
- Обновление документации

## 📝 Лицензия

Этот проект распространяется под лицензией Apache 2.0 - см. файл [LICENSE](LICENSE) для подробностей.

## 🙏 Благодарности

- [Home Assistant](https://www.home-assistant.io/) - платформа умного дома
- [OpenWakeWord](https://github.com/dscripka/openWakeWord) - библиотека распознавания wake words
- [ONNX Runtime](https://onnxruntime.ai/) - для запуска ML моделей
- Сообщество Android разработчиков

## 🐛 Известные проблемы

- Некоторые устройства могут требовать дополнительных разрешений для управления экраном
- Wake word detection может быть менее точным в шумных средах
- Батарея устройства может разряжаться быстрее при постоянном прослушивании

## 📞 Поддержка

- 📧 [Issues](https://github.com/msp1974/ViewAssist_Companion_App/issues) - для багов и фич
- 📖 [Discussions](https://github.com/msp1974/ViewAssist_Companion_App/discussions) - для вопросов и обсуждений
- 🏠 [Home Assistant Community](https://community.home-assistant.io/) - форум сообщества

## 📊 Статус проекта

[![Stars](https://img.shields.io/github/stars/msp1974/ViewAssist_Companion_App?style=social)](https://github.com/msp1974/ViewAssist_Companion_App/stargazers)
[![Forks](https://img.shields.io/github/forks/msp1974/ViewAssist_Companion_App?style=social)](https://github.com/msp1974/ViewAssist_Companion_App/fork)

---

**Примечание**: Это неофициальное приложение. Используйте на свой страх и риск.
