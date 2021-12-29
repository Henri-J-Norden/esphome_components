import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.const import CONF_ID

mi_ns = cg.esphome_ns.namespace("mi")
Mi = mi_ns.class_("Mi", cg.Component)

INTERFACE_TYPES = {
  "lt8900" : "lt8900",
  "nrf24" : "nrf24",
}

POWER_LEVELS = {
  "MIN" : "MIN",
  "LOW" : "LOW",
  "HIGH" : "HIGH",
  "MAX" : "MAX",
}

CHANNELS = {
  "LOW" : "LOW",
  "MID" : "MID",
  "HIGH" : "HIGH",
}


CONF_CE_PIN = "ce_pin"
CONF_CSN_PIN = "csn_pin"
CONF_RESET_PIN = "reset_pin"
CONF_RADIO_INTERFACE_TYPE = "radio_interface_type"
CONF_PACKET_REPEATS = "packet_repeats"
CONF_LISTEN_REPEATS = "listen_repeats"
CONF_STATE_FLUSH_INTERVAL = "state_flush_interval"
CONF_PACKET_REPEAT_THROTTLE_THRESHOLD = "packet_repeat_throttle_threshold"
CONF_PACKET_REPEAT_THROTTLE_SENSITIVITY = "packet_repeat_throttle_sensitivity"
CONF_PACKET_REPEAT_MINIMUM = "packet_repeat_minimum"
CONF_ENABLE_AUTOMATIC_MODE_SWITCHING = "enable_automatic_mode_switching"
CONF_RF24_POWER_LEVEL = "rf24_power_level"
CONF_RF24_CHANNELS = "rf24_channels"
CONF_RF24_LISTEN_CHANNEL = "rf24_listen_channel"
CONF_PACKET_REPEATS_PER_LOOP = "packet_repeats_per_loop"
  
CONF_MI_ID = "mi_id"
CONFIG_SCHEMA = (
  cv.Schema(
    {
      cv.GenerateID(): cv.declare_id(Mi),
      cv.Required(CONF_CE_PIN): pins.gpio_output_pin_schema,
      cv.Required(CONF_CSN_PIN): pins.gpio_output_pin_schema,
      cv.Optional(CONF_RESET_PIN): pins.gpio_output_pin_schema,
      cv.Optional(CONF_RADIO_INTERFACE_TYPE) : cv.enum(INTERFACE_TYPES),
      cv.Optional(CONF_PACKET_REPEATS) : cv.uint16_t,
      cv.Optional(CONF_LISTEN_REPEATS) : cv.uint8_t,
      cv.Optional(CONF_STATE_FLUSH_INTERVAL) : cv.uint16_t,
      cv.Optional(CONF_PACKET_REPEAT_THROTTLE_THRESHOLD) : cv.uint16_t,
      cv.Optional(CONF_PACKET_REPEAT_THROTTLE_SENSITIVITY) : cv.uint16_t,
      cv.Optional(CONF_PACKET_REPEAT_MINIMUM) : cv.uint16_t,
      cv.Optional(CONF_ENABLE_AUTOMATIC_MODE_SWITCHING) : cv.boolean,
      cv.Optional(CONF_RF24_POWER_LEVEL) : cv.enum(POWER_LEVELS),
      ##cv.Optional(CONF_RF24_CHANNELS) : 
      cv.Optional(CONF_RF24_LISTEN_CHANNEL) : cv.enum(CHANNELS),
      cv.Optional(CONF_PACKET_REPEATS_PER_LOOP) : cv.uint16_t,
    }
  )
  .extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    cg.add_library("SPI", None)
    cg.add_library("RF24", None)
    cg.add_library("PathVariableHandlers", None)
    cg.add_library("https://github.com/luisllamasbinaburo/Arduino-List", None)
    cg.add_library("bblanchon/ArduinoJson", None)
    
    ce_pin = await cg.gpio_pin_expression(config[CONF_CE_PIN])
    cg.add(var.set_ce_pin(ce_pin))
    csn_pin = await cg.gpio_pin_expression(config[CONF_CSN_PIN])
    cg.add(var.set_csn_pin(csn_pin))
    
    if CONF_RESET_PIN in config:
      reset_pin = await cg.gpio_pin_expression(config[CONF_RESET_PIN])
      cg.add(var.set_reset_pin(reset_pin))

    if CONF_RADIO_INTERFACE_TYPE in config:
      cg.add(var.set_radio_interface_type(radio_interface_type))
      
    if CONF_PACKET_REPEATS in config:
      cg.add(var.set_packet_repeats(packet_repeats))
      
    if CONF_LISTEN_REPEATS in config:
      cg.add(var.set_listen_repeats(listen_repeats))
      
    if CONF_STATE_FLUSH_INTERVAL in config:
      cg.add(var.set_state_flush_interval(state_flush_interval))
      
    if CONF_PACKET_REPEAT_THROTTLE_THRESHOLD in config:
      cg.add(var.set_packet_repeat_throttle_threshold(packet_repeat_throttle_threshold))
    
    if CONF_PACKET_REPEAT_THROTTLE_SENSITIVITY in config:
      cg.add(var.set_packet_repeat_throttle_sensitivity(packet_repeat_throttle_sensitivity))
      
    if CONF_PACKET_REPEAT_MINIMUM in config:
      cg.add(var.set_packet_repeat_minimum(packet_repeat_minimum))
      
    if CONF_ENABLE_AUTOMATIC_MODE_SWITCHING in config:
      cg.add(var.set_enable_automatic_mode_switching(enable_automatic_mode_switching))
      
    if CONF_RF24_POWER_LEVEL in config:
      cg.add(var.set_rf24_power_level(rf24_power_level))
      
    if CONF_RF24_LISTEN_CHANNEL in config:
      cg.add(var.set_rf24_listen_channel(rf24_listen_channel))
    
    if CONF_PACKET_REPEATS_PER_LOOP in config:
      cg.add(var.set_packet_repeats_per_loop(packet_repeats_per_loop))
