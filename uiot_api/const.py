"""Uiot const."""

from homeassistant.const import Platform

DOMAIN = "uiot_home"
COMPANY = "UIOT"
API_OPT_AUTH = "/oauth/token"

# """Production environment"""
AUTHURL = "https://polysh.unisiot.com:8165/oauth"
GATEWAY = "https://openapi.unisiot.com/gateway"
APP_KEY = "8vj99vwcn9qxk295oqmq7q3p2ni417q7"
APP_SECRET = "i6AFqgDm8Bg2m9qrvYiqW3BqRhB3NEbN"
MQTT_BROKER = "umqt.unisiot.com"
MQTT_PORT = 51322
PLATFORMS = [
    Platform.CLIMATE,
    Platform.COVER,
    Platform.FAN,
    Platform.LIGHT,
    Platform.MEDIA_PLAYER,
    Platform.SCENE,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.WATER_HEATER,
]

2521g79226894f2db093c98bc4933ffe
8vj99vwcn9qxk295oqmq7q3p2ni417q7