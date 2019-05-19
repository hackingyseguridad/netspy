tshark -Tek | jq -C 'select(.layers.gquic) | .layers.ip,.layers.gquic' | rg -v null
