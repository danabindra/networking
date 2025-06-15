# P4 Lab on Azure VMs 

## Summary
p4 switch lab running on a linux in azure 
enable monitoring grafana/prometheus/loki/alloy docker compose on local machine.

---

## Components

|                        | Description |
|------------------------|-------------|
| azure vm               | linux vm (ubuntu 22.04) running bmv2, p4 programs, mininet |
| node exporter          | exposes system and interface metrics to prometheus |
| prometheus (bare metal)| scrapes metrics from vm |
| grafana (bare metal)   | visualizes metrics with dashboards |
| networking             | port 9100 opened via nsg; bare metal host can reach vm |

---

## Functional Requirements

### 1.  Metrics 
- [ ] install node exporter 
- [ ] listen on port 9100
- [ ] inbound nsg 9100
- [ ] `systemd` node exporter

### 2. Monitor - Docker Compose
- update `prometheus.yml`:
```yaml
scrape_configs:
  - job_name: 'someazureVMs'
    static_configs:
      - targets: ['x.x.x.x:9100']
      - targets: ['x.x.x.x:9100']
      - targets: ['x.x.x.x:9100']
```
- restart prometheus:
```bash
docker compose restart prometheus
```

### 3. Dashboards (need revision once lab switches up)
- `node_network_receive_bytes_total`
- `node_cpu_seconds_total`
- `node_memory_memfree_bytes`
- `node_network_receive_errors_total`
- `instance` variable

### 4. P4 lab requirements
- [ ]  gcc, python3, pip, mininet, and git
- [ ] p4c and bmv2 from official p4lang repos
- [ ] create/test p4 programs
- [ ] run `simple_switch` with compiled json
- [ ] traffic sim w/ scapy
- [ ] collect interface metrics via node exporter
- [ ] log traffic with tcpdump and parse with loki/grafana (TBD)

---

## Non-Functional Requirements
- restrict port 9100 exposure to trusted ips
- node exporter resource usage ?
- metrics refresh interval 1m 

---

## Future Enhancements (needs work)
- DNS
- export bmv2 stats via prometheus pushgateway
- build grafana dashboards for p4  counters
- add alerting for packet drops / tx, rx failures
- tcpdump traces logs

---



| Phase                   | Target Date |
|------------------------|-------------|
| node exporter setup    | day 1  - DONE      |
| prometheus integration | day 1  - DONE     |
| grafana dashboard      | day 2  - DONE    |
|       |
| optional alerting      | day 3       |

---

## Notes
test connection with:
```bash curl http://x.x.x.x9100/metrics
```



