const config = function () {
    const configMqtt = {
        HOST_MQTT_BROKER: "ws://mqtt.hva-robots.nl/mqtt",
        MQTT_ID: "krakers",
        MQTT_PASSWORD: "kuNH5LNWptsGrPfL6Azh",
        MQTT_TOPIC_PHONE: "krakers/PAD",
        MQTT_TOPIC_PY: "krakers/PAD/NAVI",
        MQTT_TOPIC_SAY: "krakers/PAD/NAO/SAY"

    };
    return configMqtt;
}