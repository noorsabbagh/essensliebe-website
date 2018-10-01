import zomato_api, json
config={
  "user_key":"0af766e8f013b40c87691e93e0dd63a1"
}
zomato  = zomato_api.initialize_app(config)
collections = zomato.restaurant_search(latitude="-37.8620", longitude="145.2860",limit=20)
print(collections)