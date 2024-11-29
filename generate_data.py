from datetime import date
from werkzeug.security import generate_password_hash
from models import Base, RecipePost, User, Comment, DietaryChoice, TimeSpent, MealCost, MealTime


def generate_example_data(db):
    # Check if user with id=1 exists, if not, create it
    user = db.session.get(User, 1)

    if not user:
        admin_user = User(
            id=1,
            email="admin@gmail.com",
            password=generate_password_hash("123", method='pbkdf2:sha256', salt_length=8),
            name="Admin User"
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created with id=1.")

    # Check if the 'RecipePost' table is empty
    if not db.session.query(RecipePost).first():
        # Insert Example Data
        example_posts = [
            RecipePost(
                author_id=1,
                title="Classic Spaghetti Carbonara",
                subtitle="A traditional Italian pasta dish",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Spaghetti, eggs, Parmesan cheese, pancetta, black pepper, salt.",
                instructions="1. Cook spaghetti. 2. Whisk eggs and cheese. 3. Fry pancetta. 4. Toss all together.",
                img_url="https://static01.nyt.com/images/2021/02/14/dining/carbonara-horizontal/carbonara-horizontal-videoSmall-v2.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Chicken Tikka Masala",
                subtitle="Creamy, spicy Indian-style curry",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Chicken, yogurt, cream, tomato paste, garam masala, garlic, ginger, chili.",
                instructions="1. Marinate chicken. 2. Cook chicken and set aside. 3. Prepare sauce and combine.",
                img_url="https://www.allrecipes.com/thmb/36BXoF_6WCYV2T6f_bM-5bX8yfw=/0x512/filters:no_upscale():max_bytes(150000):strip_icc()/239867chef-johns-chicken-tikka-masala-ddmfs-3X4-0572-e02a25f8c7b745459a9106e9eb13de10.jpg",
                dietary_choice=DietaryChoice.HIGH_PROTEIN,
                time_spent=TimeSpent.MEAL_PREP,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Vegetarian Chili",
                subtitle="A hearty and healthy chili",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Beans, tomatoes, onions, bell peppers, garlic, spices, corn.",
                instructions="1. Sauté veggies. 2. Add beans and tomatoes. 3. Simmer and serve.",
                img_url="https://cookieandkate.com/images/2015/11/best-vegetarian-chili-1-1.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Margherita Pizza",
                subtitle="A simple classic Italian pizza",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Pizza dough, tomatoes, mozzarella, basil, olive oil, salt.",
                instructions="1. Spread tomato sauce on dough. 2. Add mozzarella and basil. 3. Bake.",
                img_url="https://ca.ooni.com/cdn/shop/articles/20220211142645-margherita-9920.jpg?crop=center&height=800&v=1661341987&width=800",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Pancakes",
                subtitle="Fluffy and light breakfast pancakes",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Flour, eggs, milk, sugar, baking powder, butter, syrup.",
                instructions="1. Mix ingredients. 2. Cook batter in skillet. 3. Serve with syrup.",
                img_url="https://www.allrecipes.com/thmb/hB7uGW06pqyk6hApOfGxk5kG4SI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/21014-Good-old-Fashioned-Pancakes-mfs_001-1-8fc3e06998fe4fe8b5f2ad6ba7e8ad46.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.BREAKFAST
            ),
            RecipePost(
                author_id=1,
                title="Greek Salad",
                subtitle="Fresh and vibrant Mediterranean salad",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Cucumber, tomatoes, onions, feta cheese, olives, olive oil, oregano.",
                instructions="1. Chop veggies. 2. Toss with feta, olives, and dressing. 3. Serve chilled.",
                img_url="https://www.italianbellavita.com/wp-content/uploads/2022/08/739C7136-CBA2-4DDC-8D56-ECA409F69AB9.jpeg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Beef Stroganoff",
                subtitle="Creamy, savory Russian-style beef",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Beef, mushrooms, onions, sour cream, broth, noodles, flour.",
                instructions="1. Cook beef and mushrooms. 2. Prepare creamy sauce. 3. Combine with noodles.",
                img_url="https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/k%2FPhoto%2FRecipes%2F2024-03-beef-stroganoff-190%2Fbeef-stroganoff-190-342_1",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Teriyaki Salmon",
                subtitle="Sweet and savory glazed salmon",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Salmon, soy sauce, honey, garlic, ginger, sesame seeds.",
                instructions="1. Marinate salmon. 2. Bake or pan-sear. 3. Garnish with sesame seeds.",
                img_url="https://www.allrecipes.com/thmb/a2Pgu3Q5z92A79zUrEISwGRqfAI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/228285teriyaki-salmonFranceC4x3-495e53221ca54183bf0ff5b2fa5aae55.jpg",
                dietary_choice=DietaryChoice.HIGH_PROTEIN,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Banana Bread",
                subtitle="Moist and flavorful quick bread",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Bananas, flour, sugar, butter, eggs, baking soda, vanilla extract.",
                instructions="1. Mash bananas. 2. Mix wet and dry ingredients. 3. Bake in loaf pan.",
                img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ384-Gtmd0lPVnKrXahqVCmEDiog_SzA-KrQ&s",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.BREAKFAST
            ),
            RecipePost(
                author_id=1,
                title="Guacamole",
                subtitle="Creamy and delicious avocado dip",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Avocados, lime juice, onions, tomatoes, cilantro, salt.",
                instructions="1. Mash avocados. 2. Mix with lime, onions, and tomatoes. 3. Serve with chips.",
                img_url="https://www.allrecipes.com/thmb/p4OH2iCMjg6-cgzI__Nwn9VR-r0=/0x512/filters:no_upscale():max_bytes(150000):strip_icc()/AR-RM-14064-easy-guacamole-ddmfs-3x4-9e4a1eb1bb34421a99db675b53a29e53.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Quinoa Salad with Lemon Dressing",
                subtitle="A light and refreshing plant-based salad",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Quinoa, cucumbers, tomatoes, red onion, parsley, lemon, olive oil, salt.",
                instructions="1. Cook quinoa and let it cool. 2. Chop veggies. 3. Mix all with dressing.",
                img_url="https://www.silverspringfoods.com/assets/images/2020/06/large/177-quinoa-salad-with-lemon-dijon-vinaigrette.webp",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Grilled Chicken Caesar Salad",
                subtitle="A protein-packed classic salad",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Chicken breast, Romaine lettuce, croutons, Parmesan cheese, Caesar dressing.",
                instructions="1. Grill chicken. 2. Chop lettuce and mix with dressing. 3. Top with chicken.",
                img_url="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2023/08/Grilled-Chicken-Caesar-Salad-11.jpg",
                dietary_choice=DietaryChoice.HIGH_PROTEIN,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Vegan Buddha Bowl",
                subtitle="A nutritious and colorful vegan meal",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Brown rice, sweet potatoes, chickpeas, spinach, avocado, tahini dressing.",
                instructions="1. Roast sweet potatoes. 2. Cook rice. 3. Assemble with toppings and dressing.",
                img_url="https://simplyceecee.co/wp-content/uploads/2018/07/veganbuddhabowl-2.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Shrimp Stir-Fry",
                subtitle="A quick and healthy seafood dinner",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Shrimp, broccoli, carrots, bell peppers, soy sauce, garlic, ginger, sesame oil.",
                instructions="1. Sauté veggies. 2. Add shrimp and stir-fry with sauce. 3. Serve over rice.",
                img_url="https://images.themodernproper.com/billowy-turkey/production/posts/Garlic-Shrimp-Stir-Fry-14.jpg?w=960&h=960&q=82&fm=jpg&fit=crop&dm=1599766557&s=010101ec061e6afa587162f05ca8e352",
                dietary_choice=DietaryChoice.HIGH_PROTEIN,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Classic Omelette",
                subtitle="A quick and versatile breakfast option",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Eggs, milk, cheese, ham, bell peppers, salt, pepper.",
                instructions="1. Whisk eggs with milk. 2. Cook in a skillet with fillings. 3. Fold and serve.",
                img_url="https://www.seriouseats.com/thmb/FWfGvovlGhKamgLyj-Jf1Tjh0IM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2016__04__20160323-french-omelet-vicky-wasik--29-4443fd8d1f5b4e359f31e384d901cefb.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.BREAKFAST
            ),
            RecipePost(
                author_id=1,
                title="Stuffed Bell Peppers",
                subtitle="A hearty and colorful main dish",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Bell peppers, ground turkey, rice, tomatoes, cheese, onion, spices.",
                instructions="1. Hollow out peppers. 2. Prepare filling with meat and rice. 3. Bake with cheese.",
                img_url="https://www.dinneratthezoo.com/wp-content/uploads/2019/06/stuffed-bell-peppers-4.jpg",
                dietary_choice=DietaryChoice.LOW_CARB,
                time_spent=TimeSpent.MEAL_PREP,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Avocado Toast",
                subtitle="A trendy and nutritious breakfast option",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Whole-grain bread, avocado, lemon juice, chili flakes, salt.",
                instructions="1. Toast bread. 2. Mash avocado with lemon juice. 3. Spread on toast and season.",
                img_url="https://www.eatingbirdfood.com/wp-content/uploads/2023/12/avocado-toast-hero-cropped-500x500.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.BREAKFAST
            ),
            RecipePost(
                author_id=1,
                title="Beef and Broccoli",
                subtitle="A simple and flavorful stir-fry",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Beef strips, broccoli, soy sauce, garlic, ginger, cornstarch, rice.",
                instructions="1. Cook beef. 2. Stir-fry broccoli. 3. Combine with sauce and serve over rice.",
                img_url="https://www.justataste.com/wp-content/uploads/2018/04/beef-broccoli-sauce-1.jpg",
                dietary_choice=DietaryChoice.HIGH_PROTEIN,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Caprese Salad",
                subtitle="A simple and fresh Italian appetizer",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Tomatoes, mozzarella, basil, balsamic glaze, olive oil, salt.",
                instructions="1. Slice tomatoes and mozzarella. 2. Layer with basil. 3. Drizzle with oil and balsamic.",
                img_url="https://downshiftology.com/wp-content/uploads/2019/07/How-to-Make-Caprese-Salad-1.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.SNACK
            ),
            RecipePost(
                author_id=1,
                title="Vegetable Soup",
                subtitle="A comforting and nutritious soup",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Carrots, celery, onions, tomatoes, broth, garlic, thyme, bay leaf.",
                instructions="1. Sauté vegetables. 2. Add broth and seasonings. 3. Simmer until tender.",
                img_url="https://www.allrecipes.com/thmb/wYELcGueAb7YS20dQ95t22T1CDs=/0x512/filters:no_upscale():max_bytes(150000):strip_icc()/13338-quick-and-easy-vegetable-soup-DDMFS-4x3-402702f59e7a41519515cecccaba1b80.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="BBQ Pulled Pork Sandwiches",
                subtitle="Tender pulled pork on a soft bun",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Pork shoulder, BBQ sauce, buns, coleslaw, pickles.",
                instructions="1. Slow cook pork with BBQ sauce. 2. Shred and serve on buns with coleslaw.",
                img_url="https://saltpepperskillet.com/wp-content/uploads/pulled-pork-sandwiches-on-butcher-paper-horizontal.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.SPECIAL_OCCASION,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Tofu Stir-Fry",
                subtitle="A plant-based protein-packed stir-fry",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Tofu, broccoli, carrots, soy sauce, ginger, garlic, sesame oil.",
                instructions="1. Pan-fry tofu. 2. Stir-fry veggies. 3. Combine with sauce and serve.",
                img_url="https://rainbowplantlife.com/wp-content/uploads/2023/01/tofu-stir-fry-cover-photo-1-of-1.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Egg Salad Sandwiches",
                subtitle="A creamy and quick lunch option",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Eggs, mayonnaise, mustard, salt, pepper, bread.",
                instructions="1. Boil eggs and chop. 2. Mix with mayo and mustard. 3. Assemble sandwiches.",
                img_url="https://www.spendwithpennies.com/wp-content/uploads/2023/03/1200-Best-Egg-Salad-Recipe-SpendWithPennies.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Lentil Curry",
                subtitle="A hearty and spicy vegan dish",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Lentils, coconut milk, tomatoes, curry spices, garlic, ginger.",
                instructions="1. Cook lentils. 2. Prepare curry sauce. 3. Combine and simmer.",
                img_url="https://www.skinnytaste.com/wp-content/uploads/2023/05/Lentil-Curry-7.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Baked Ziti",
                subtitle="Cheesy and comforting Italian-American pasta",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Ziti pasta, marinara sauce, ricotta cheese, mozzarella, Parmesan.",
                instructions="1. Cook pasta. 2. Layer with sauce and cheeses. 3. Bake until bubbly.",
                img_url="https://www.simplyrecipes.com/thmb/uGmTDCSeJB4Ac2-M4h62-FCgmu0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Baked-Ziti-LEAD-db0d2e1b6e554b4aa6ff8a2f23f2f903.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.SPECIAL_OCCASION,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Fruit Parfait",
                subtitle="A light and healthy breakfast or snack",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Yogurt, granola, mixed berries, honey.",
                instructions="1. Layer yogurt, berries, and granola in a cup. 2. Drizzle with honey.",
                img_url="https://www.simplysissom.com/wp-content/uploads/2017/01/horizontalparfaityogurt-copy.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.BREAKFAST
            ),
            RecipePost(
                author_id=1,
                title="Chickpea Salad Wraps",
                subtitle="A quick and healthy plant-based wrap",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Chickpeas, avocado, lemon, garlic, tortillas, spinach.",
                instructions="1. Mash chickpeas with avocado and season. 2. Spread on tortillas with spinach. 3. Roll and serve.",
                img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZcMaE8yYiotmkZpdPi7ZkXsqB1z3TPCwQHQ&s",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Roasted Cauliflower Tacos",
                subtitle="Flavorful and plant-based tacos",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Cauliflower, taco seasoning, tortillas, salsa, avocado, lime.",
                instructions="1. Roast cauliflower with seasoning. 2. Assemble tacos with toppings. 3. Serve warm.",
                img_url="https://cdn.loveandlemons.com/wp-content/uploads/2021/04/cauliflower-tacos.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.BALANCED,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Turkey Meatballs",
                subtitle="Lean and flavorful meatballs for any occasion",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Ground turkey, breadcrumbs, eggs, Parmesan, garlic, marinara sauce.",
                instructions="1. Mix ingredients and form meatballs. 2. Bake or fry. 3. Serve with sauce.",
                img_url="https://www.culinaryhill.com/wp-content/uploads/2018/06/Turkey-Meatballs-Culinary-Hill-square-500x375.jpg",
                dietary_choice=DietaryChoice.LOW_CARB,
                time_spent=TimeSpent.MEAL_PREP,
                meal_cost=MealCost.MODERATE,
                meal_time=MealTime.DINNER
            ),
            RecipePost(
                author_id=1,
                title="Blueberry Muffins",
                subtitle="Soft and sweet breakfast muffins",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Blueberries, flour, sugar, butter, eggs, baking powder.",
                instructions="1. Mix dry and wet ingredients separately. 2. Combine and fold in blueberries. 3. Bake in muffin tin.",
                img_url="https://www.kingarthurbaking.com/sites/default/files/styles/featured_image/public/2022-12/KABC_Quick-Breads_Blueberry-Muffin_08304.jpg?itok=EM7XxPfL",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.BREAKFAST
            ),
            RecipePost(
                author_id=1,
                title="Falafel",
                subtitle="Crispy and flavorful chickpea patties",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Chickpeas, parsley, onion, garlic, flour, spices, oil for frying.",
                instructions="1. Blend chickpeas and seasonings. 2. Form into patties and fry. 3. Serve with pita and tahini.",
                img_url="https://toriavey.com/images/2011/01/TOA109_18-1-500x500.jpeg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.MEAL_PREP,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.LUNCH
            ),
            RecipePost(
                author_id=1,
                title="Mango Smoothie",
                subtitle="A refreshing tropical drink",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Mango, banana, yogurt, orange juice, ice cubes.",
                instructions="1. Combine all ingredients in a blender. 2. Blend until smooth. 3. Serve chilled.",
                img_url="https://cdn.loveandlemons.com/wp-content/uploads/2023/05/mango-smoothie.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.QUICK,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.SNACK
            ),
            RecipePost(
                author_id=1,
                title="Baked Sweet Potato Fries",
                subtitle="Crispy and healthy alternative to fries",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Sweet potatoes, olive oil, paprika, garlic powder, salt.",
                instructions="1. Slice sweet potatoes. 2. Toss with oil and spices. 3. Bake until crispy.",
                img_url="https://www.cookingclassy.com/wp-content/uploads/2021/10/baked-sweet-potato-fries-12.jpg",
                dietary_choice=DietaryChoice.PLANT_BASED,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.SUPER_BUDGET,
                meal_time=MealTime.SNACK
            ),
            RecipePost(
                author_id=1,
                title="Chocolate Chip Cookies",
                subtitle="Classic soft and chewy cookies",
                date=date.today().strftime("%B %d, %Y"),
                ingredients="Butter, sugar, eggs, flour, chocolate chips, baking soda.",
                instructions="1. Cream butter and sugar. 2. Mix in dry ingredients and chocolate chips. 3. Bake on cookie sheet.",
                img_url="https://static01.nyt.com/images/2022/02/12/dining/JT-Chocolate-Chip-Cookies/JT-Chocolate-Chip-Cookies-googleFourByThree-v2.jpg",
                dietary_choice=DietaryChoice.EVERYTHING,
                time_spent=TimeSpent.SIMPLE,
                meal_cost=MealCost.AFFORDABLE,
                meal_time=MealTime.SNACK
            )
        ]

        # Add all example posts to the session
        db.session.add_all(example_posts)
        db.session.commit()
