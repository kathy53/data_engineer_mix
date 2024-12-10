import datetime

class Property:
    crawl_date = datetime.datetime.now().strftime("%Y-%m-%d")
    def __init__(self, title, json_script, price, community_fees, building_area, surface_area, publication_date, images_urls, publisher_name, publisher_phone, publisher_url, condition, construction_year, secondary_json, secondary_description, facilities, nearby_locations, item_url, state, kind) :
        self.title = title
        self.json_script = json_script
        self.price = price
        self.cmunity_fees = community_fees
        self.building_area = building_area
        self.surface_area = surface_area
        self.publication_date = publication_date 
        self.images_urls = images_urls
        self.publisher_name = publisher_name
        self.publisher_phone = publisher_phone
        self.publisher_url = publisher_url
        self.condition = condition
        self.construction_year = construction_year
        self.secondary_json = secondary_json
        self.secondary_description = secondary_description
        self.facilities = facilities
        self.nearby_locations = nearby_locations
        self.item_url = item_url
        self.state = state
        self.kind = kind
    def __str__(self):
        return f"This is a property crawled from {self.item_url}"
    
property = Property(
    title="Casa en venta",
    json_script='{"description":"This is a dummy data"}',
    price=100000,
    community_fees=1000,
    building_area=100,
    surface_area=100,
    publication_date="2021-01-01",
    images_urls=["url1", "url2"],
    publisher_name="This is a dummy name",
    publisher_phone="4559692475",
    publisher_url="publisher_url",
    condition="Good",
    construction_year="1996",
    secondary_json="secondary_json",
    secondary_description="This is a secondary_description",
    facilities='[kitchen, pool, 4 bedrooms"]',
    nearby_locations="[school, park, market]",
    item_url="https:dummysite.com/location/casa",
    state="Morelos",
    kind="casa"
)
print(property)