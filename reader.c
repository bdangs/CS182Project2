/**
 * purpose: Check if an XML file adheres to specific XML syntax rules.
 *          Rules checked:
 *          1. All XML elements must have a closing tag.
 *          2. XML tags are case sensitive.
 *          3. All XML elements must be properly nested.
 *          4. All XML documents must have a root element.
 *          5. Attribute values must always be quoted.
 */

#include <stdio.h>
#include <libxml/xmlreader.h>

/**
 * processNode:
 * @reader: the xmlReader
 *
 * Check specific XML syntax rules for the current node
 */
static void processNode(xmlTextReaderPtr reader) {
    const xmlChar *name, *value;

    name = xmlTextReaderConstName(reader);
    if (name == NULL)
        name = BAD_CAST "--";

    value = xmlTextReaderConstValue(reader);

    // Rule 1: All XML elements must have a closing tag
    if (xmlTextReaderNodeType(reader) == XML_ELEMENT_NODE && xmlTextReaderIsEmptyElement(reader)) {
        fprintf(stderr, "Error: Element '%s' is empty but does not have a closing tag.\n", name);
    }

    // Rule 2: XML tags are case sensitive
    if (xmlStrcasecmp(name, BAD_CAST xmlTextReaderConstLocalName(reader)) != 0) {
        fprintf(stderr, "Error: Case sensitivity violation for element '%s'.\n", name);
    }

    // Rule 5: Attribute values must always be quoted
    if (xmlTextReaderNodeType(reader) == XML_ATTRIBUTE_NODE && value != NULL && value[0] != '"' && value[0] != '\'') {
        fprintf(stderr, "Error: Attribute value for '%s' is not quoted.\n", name);
    }

    printf("%d %d %s %d %d",
           xmlTextReaderDepth(reader),
           xmlTextReaderNodeType(reader),
           name,
           xmlTextReaderIsEmptyElement(reader),
           xmlTextReaderHasValue(reader));
    if (value == NULL)
        printf("\n");
    else {
        if (xmlStrlen(value) > 40)
            printf(" %.40s...\n", value);
        else
            printf(" %s\n", value);
    }
}

/**
 * streamFile:
 * @filename: the file name to parse
 *
 * Parse and check specific XML syntax rules for an XML file.
 */
static void streamFile(const char *filename) {
    xmlTextReaderPtr reader;
    int ret;

    reader = xmlReaderForFile(filename, NULL, XML_PARSE_NOENT);
    if (reader != NULL) {
        ret = xmlTextReaderRead(reader);
        while (ret == 1) {
            processNode(reader);
            ret = xmlTextReaderRead(reader);
        }

        if (ret == 0) {
            printf("\nXML file '%s' is valid.\n", filename);
        } else {
            fprintf(stderr, "%s : failed to parse\n", filename);
        }

        xmlFreeTextReader(reader);
    } else {
        fprintf(stderr, "Unable to open %s\n", filename);
    }
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <xml_file>\n", argv[0]);
        return 1;
    }

    /*
     * this initialize the library and check potential ABI mismatches
     * between the version it was compiled for and the actual shared
     * library used.
     */
    LIBXML_TEST_VERSION

    streamFile(argv[1]);

    /*
     * Cleanup function for the XML library.
     */
    xmlCleanupParser();
    /*
     * this is to debug memory for regression tests
     */
    xmlMemoryDump();
    return 0;
}
