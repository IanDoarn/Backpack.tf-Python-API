# pybptf
Python wrapper for backpack.tf API

# Requirements
 - Python 3.5+
 - requests
 - backpack.tf API Key

# Install
```commandline
python setup.py install
```

# Usage
```python
from pybptf.bptf.webcalls.special_items import SpecialItems

sp = SpecialItems(<YOUR API KEY HERE>)

print(sp.data)
```

Result

```json
{
    "response": {
        "success": 1,
        "current_time": 1488666707,
        "items": [
            {
                "name": "Random Craft Hat",
                "item_name": "Random Craft Hat",
                "defindex": -2,
                "item_class": "tf_wearable",
                "item_type_name": "Currency Item",
                "item_description": "Any item that is considered to be a random craft hat.",
                "item_quality": 0,
                "min_ilevel": 1,
                "max_ilevel": 1,
                "image_url": "https:\/\/steamcdn-a.akamaihd.net\/apps\/440\/icons\/kit_fancyhats.bf5ba4ea973728df20402c0c9a4737f18d5d560c.png",
                "image_url_large": "https:\/\/steamcdn-a.akamaihd.net\/apps\/440\/icons\/kit_fancyhats_large.800ea1b16df707ffa27f9f6e6033e8ba3f0f5333.png",
                "appid": 440
            }
        ]
    }
}
```