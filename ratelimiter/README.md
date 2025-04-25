# Install in rate namespace
helm install ratelimiter-release ./ratelimiter -n rate

# Install with default and desire values in dev namespace
helm install ratelimiter-release ./ratelimiter --values ratelimiter/values.yaml -f ratelimiter/values-dev.yaml -n dev

# to Upgrade the helm
helm upgrade ratelimiter-release ./ratelimiter --values ratelimiter/values.yaml -n rate

# to see what changes when upgrade
helm template ratelimiter-release ./ratelimiter --values ratelimiter/values.yaml -n rate

# list all helm package
helm ls --all-namespaces
