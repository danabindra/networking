/L3 switch1 */

#include <core.p4>
#include <v1model.p4>

header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

header ipv4_t {
    bit<4>  version;
    bit<4>  ihl;
    bit<8>  diffserv;
    bit<16> totalLen;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragOffset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> hdrChecksum;
    bit<32> srcAddr;
    bit<32> dstAddr;
}

struct headers {
    ethernet_t ethernet;
    ipv4_t     ipv4;
}

struct metadata 

parser dbParser(packet_in pkt, out headers hdr, inout metadata meta, inout standard_metadata_t standard_metadata) {
    state start {
        pkt.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            0x0800: parse_ipv4;
            default: accept;
        }
    }

    state parse_ipv4 {
        pkt.extract(hdr.ipv4);
        transition accept;
    }
}

control dbVerifyChecksum(...) { apply {} }
control dbIngress(...) { apply {} }
control dbEgress(...) { apply {} }
control dbComputeChecksum(...) { apply {} }

control dbDeparser(packet_out pkt, in headers hdr) {
    apply {
        pkt.emit(hdr.ethernet);
        pkt.emit(hdr.ipv4);
    }
}

V1Switch(dbParser(),
         dbVerifyChecksum(),
         dbIngress(),
         dbEgress(),
         dbComputeChecksum(),
         dbDeparser()) main;
