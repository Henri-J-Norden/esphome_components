import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c_esp32
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c_esp32"]

itho_ns = cg.esphome_ns.namespace("itho")
Itho = itho_ns.class_("Itho", cg.Component, i2c_esp32.I2CDevice)

SYSSHT30_VALUES = {
  "enable" : 2,
  "disable" : 1,
}

CONF_SYSSHT30_VALUE = "syssht30"

CONF_ITHO_ID = "itho_id"
CONFIG_SCHEMA = (
  cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(Itho),
        cv.Optional(CONF_SYSSHT30_VALUE) : cv.enum(SYSSHT30_VALUES),
    }
  )
  .extend(cv.COMPONENT_SCHEMA)
  .extend(i2c_esp32.i2c_device_schema(0x40))
)

async def to_code(config):
  var = cg.new_Pvariable(config[CONF_ID])
  await cg.register_component(var, config)
  await i2c_esp32.register_i2c_device(var, config)
  
  cg.add_library("Ticker", None)
  cg.add_library("ArduinoJson", None)
  
  if CONF_SYSSHT30_VALUE in config:
    cg.add(var.setSysSHT30(config[CONF_SYSSHT30_VALUE]))