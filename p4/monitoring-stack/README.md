# Monitoring Stack

This is a complete monitoring stack using Grafana, Prometheus, Loki, Alertmanager, and Grafana Alloy.

## Services

- **Grafana**: Visualization platform (http://localhost:3000)
- **Prometheus**: Metrics collection and storage (http://localhost:9090)
- **Loki**: Log aggregation (http://localhost:3100)
- **Alertmanager**: Alert handling (http://localhost:9093)
- **Grafana Alloy**: Metrics and logs collection agent (http://localhost:12345)

## Getting Started

1. Start the stack:
   ```bash
   docker compose up -d
   ```

2. Access Grafana:
   - URL: http://localhost:3000
   - Default credentials: admin/admin

3. Access Prometheus:
   - URL: http://localhost:9090

4. Access Alertmanager:
   - URL: http://localhost:9093

## Configuration

- Grafana datasources are automatically configured
- Prometheus is configured to scrape metrics from all services
- Loki is configured to collect logs
- Alertmanager is configured with basic alert routing

## Directory Structure

```
monitoring-stack/
├── alertmanager/
│   └── alertmanager.yml
├── alloy/
│   └── config.alloy
├── grafana/
│   └── provisioning/
│       ├── dashboards/
│       └── datasources/
├── loki/
│   ├── loki-config.yaml
│   └── rules/
├── prometheus/
│   ├── prometheus.yml
│   └── rules/
└── docker-compose.yaml
``` 