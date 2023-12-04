import config
import functions

functions.xml_declaration(config.xsd)
functions.header(config.xsd)
functions.print_list(config.data)
functions.footer(config.xsd)
