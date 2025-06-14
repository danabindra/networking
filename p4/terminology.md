# Notes

Will clean spelling errors, formatting etc. Once I am  finished all terms



p4 switch is different from a entrp switch,  its data plane isn't pre-defined it's set by a p4 program when the switch starts the switch doesn’t come with prior knowledge of  protocols (like BGP, OSPF tables). the control plane still talks to the data plane like usual, but the tables and objects it uses are now created by the p4 code not hardcoded. this makes p4 protocl independent but still able to define  different protocols and behavior

- **architechture**  
  bunch of parts that can be programmed w/ p4 like parser, control blocks, externs

- **base type**  
  simple data types like `bit`, `bool`, `error`, `match_kind`, `void`

- **bmv2**  
  the fake switch thing used in examples; good 4 learning


  

- **control flow**  
  the logic steps p4 uses to do stuff on packets

- **control block**  
  block of code that runs the actual processing (like tables n actions)

- **data plane**  
  where packets get handled, all defined in p4 (runs fast!)

- **control plane**  
  not p4 — it's the outside thingy that sets up table rules, configs, etc.




- **deparser**  
  puts the packet back together before sending it out

- **extern**  
  some pre-built thing you call from p4, like checksum or 

- **header type**  
  tells p4 what headers look like (like ethernet, ipv4)

- **header stack**  
  bunch of headers in a row, like mpls stack or vlan

- **header union**  
  one-of-many header choices, only 1 is valid at a time

- **intrinsic metadata**  
  built-in info like ingress_port, from the switch/target

- **user metadata**  
  stuff u define urself to track state or info in the packet

- **match-action unit**  
  key part of the pipeline — checks table and runs action

- **table**  
  list of matches + actions. has keys, size, default, etc.

- **match kind**  
  type of match — `exact`, `ternary`, `lpm`, etc.


  

- **key**  
  what p4 uses to match — could be src ip, port, whatever

- **action**

- 
  does stuff like drop, forward, or change a field

- **parser**  
  finds headers in packet, kind of like a state machine

- **parser state**  
  points in the parsing process — like `start`, `accept`, etc.

- **extract**  
  pull headers from the packet in the parser

- **transition**  
  go from one parse state to the next one

- **verify**  
  check if headers are correct. throws error if not.

- **deparser pipe**  
  emits headers in order to rebuild packet

- **packet**  
  the whole data thing we’re working with


