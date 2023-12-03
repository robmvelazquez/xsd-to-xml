import config
import functions


functions.xml_declaration(config.xsd)
functions.header(config.xsd)
functions.print_elements_names(config.abstract)
functions.footer(config.xsd)
functions.print_items_to_xml(config.items_list)

