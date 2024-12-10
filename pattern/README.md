# File stucture and usage of a pository pattern 

Create the next file structureand supose the applcation service would be an API 

        your_project/
        |- app
        |   |- __init__.py
            |- models/
                |- __init__.py
                |- property.py # Base Model definition of property
            |- repositories/
                |- __init__.py
                |- base_repository.py # Abstract repository definition
            |- adapters/
                |- local_repository.py # Local implementation of the repository pattern
            |- services/
                |- api/
                    |- __init__.y
                    |- property_api.py # Service use of the repository  
        |- tests/
        |- requirements.txt
        |- README.md