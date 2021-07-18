#!/bin/bash
json_inc=$(curl --location --request GET 'api.coincap.io/v2/rates/bitcoin');

coincap_id=$(echo "$json_inc" | jq -r ".data.id");
coincap_symbol=$(echo "$json_inc" | jq -r ".data.symbol");
coincap_currentSymbol=$(echo "$json_inc" | jq -r ".data.currencySymbol");
coincap_type=$(echo "$json_inc" | jq -r ".data.type");
coincap_rateUsd=$(echo "$json_inc" | jq -r ".data.rateUsd");
coincap_timestamp=$(echo "$json_inc" | jq -r ".timestamp");

# echo {$coincap_id,$coincap_rateUsd,$coincap_timestamp};

query_ins="INSERT INTO public.bitcoin_course (id, symbol, currencysymbol, type, rateusd, timestamp) VALUES ('$coincap_id', '$coincap_symbol', '$coincap_currentSymbol', '$coincap_type', '$coincap_rateUsd', $coincap_timestamp);"

echo $query_ins;
