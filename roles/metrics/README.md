## Metrics role

Configures the following services on a host via Docker.

### Prometheus

Time-series database and metrics collector. See [prometheus.io](https://prometheus.io/).

### Exporters

Various exporters are used to expose metrics from other systems to prometheus.

#### Blackbox Exporter

Blackbox probe monitoring - uses ICMP & HTTP to establish outside healthiness and latencies of managed services (on other boxes). Also handy for certificate expiry monitoring. See [project repo](https://github.com/prometheus/blackbox_exporter).

#### UNMS Exporter

Exposes metrics collected by [UNMS](https://unms.com/) to Prometheus. Can monitor most Ubiquiti EdgeMax & AirMax devices. Very handy for network monitoring. See [project repo](https://github.com/ffddorf/unms-exporter).

### Grafana

Dashboard manager - queries Prometheus for metrics. See [grafana.com](https://grafana.com/).

### Traefik

Ingress & reverse-proxy - HTTP proxy for all public-facing services. See [Documentation](https://doc.traefik.io/traefik/).

Provides automated TLS cert provisioning via LetsEncrypt.
