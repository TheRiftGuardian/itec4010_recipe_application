from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from models import Base, RecipePost, User, Comment


def generate_example_data(db):


        # Check if user with id=1 exists, if not, create it
        # user = db.session.query(User).get(1)
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
                    img_url="https://static01.nyt.com/images/2021/02/14/dining/carbonara-horizontal/carbonara-horizontal-videoSmall-v2.jpg"
                ),
                RecipePost(
                    author_id=1,
                    title="Chicken Tikka Masala",
                    subtitle="Creamy, spicy Indian-style curry",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Chicken, yogurt, cream, tomato paste, garam masala, garlic, ginger, chili.",
                    instructions="1. Marinate chicken. 2. Cook chicken and set aside. 3. Prepare sauce and combine.",
                    img_url="https://www.allrecipes.com/thmb/36BXoF_6WCYV2T6f_bM-5bX8yfw=/0x512/filters:no_upscale():max_bytes(150000):strip_icc()/239867chef-johns-chicken-tikka-masala-ddmfs-3X4-0572-e02a25f8c7b745459a9106e9eb13de10.jpg"
                ),
                RecipePost(
                    author_id=1,
                    title="Vegetarian Chili",
                    subtitle="A hearty and healthy chili",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Beans, tomatoes, onions, bell peppers, garlic, spices, corn.",
                    instructions="1. Sauté veggies. 2. Add beans and tomatoes. 3. Simmer and serve.",
                    img_url="https://cookieandkate.com/images/2015/11/best-vegetarian-chili-1-1.jpg"
                ),
                RecipePost(
                    author_id=1,
                    title="Margherita Pizza",
                    subtitle="A simple classic Italian pizza",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Pizza dough, tomatoes, mozzarella, basil, olive oil, salt.",
                    instructions="1. Spread tomato sauce on dough. 2. Add mozzarella and basil. 3. Bake.",
                    img_url="https://ca.ooni.com/cdn/shop/articles/20220211142645-margherita-9920.jpg?crop=center&height=800&v=1661341987&width=800"
                ),
                RecipePost(
                    author_id=1,
                    title="Pancakes",
                    subtitle="Fluffy and light breakfast pancakes",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Flour, eggs, milk, sugar, baking powder, butter, syrup.",
                    instructions="1. Mix ingredients. 2. Cook batter in skillet. 3. Serve with syrup.",
                    img_url="https://www.allrecipes.com/thmb/hB7uGW06pqyk6hApOfGxk5kG4SI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/21014-Good-old-Fashioned-Pancakes-mfs_001-1-8fc3e06998fe4fe8b5f2ad6ba7e8ad46.jpg"
                ),
                RecipePost(
                    author_id=1,
                    title="Greek Salad",
                    subtitle="Fresh and vibrant Mediterranean salad",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Cucumber, tomatoes, onions, feta cheese, olives, olive oil, oregano.",
                    instructions="1. Chop veggies. 2. Toss with feta, olives, and dressing. 3. Serve chilled.",
                    img_url="https://www.italianbellavita.com/wp-content/uploads/2022/08/739C7136-CBA2-4DDC-8D56-ECA409F69AB9.jpeg"
                ),
                RecipePost(
                    author_id=1,
                    title="Beef Stroganoff",
                    subtitle="Creamy, savory Russian-style beef",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Beef, mushrooms, onions, sour cream, broth, noodles, flour.",
                    instructions="1. Cook beef and mushrooms. 2. Prepare creamy sauce. 3. Combine with noodles.",
                    img_url="https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_4:3/k%2FPhoto%2FRecipes%2F2024-03-beef-stroganoff-190%2Fbeef-stroganoff-190-342_1"
                ),
                RecipePost(
                    author_id=1,
                    title="Teriyaki Salmon",
                    subtitle="Sweet and savory glazed salmon",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Salmon, soy sauce, honey, garlic, ginger, sesame seeds.",
                    instructions="1. Marinate salmon. 2. Bake or pan-sear. 3. Garnish with sesame seeds.",
                    img_url="https://www.allrecipes.com/thmb/a2Pgu3Q5z92A79zUrEISwGRqfAI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/228285teriyaki-salmonFranceC4x3-495e53221ca54183bf0ff5b2fa5aae55.jpg"
                ),
                RecipePost(
                    author_id=1,
                    title="Banana Bread",
                    subtitle="Moist and flavorful quick bread",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Bananas, flour, sugar, butter, eggs, baking soda, vanilla extract.",
                    instructions="1. Mash bananas. 2. Mix wet and dry ingredients. 3. Bake in loaf pan.",
                    img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ384-Gtmd0lPVnKrXahqVCmEDiog_SzA-KrQ&s"
                ),
                RecipePost(
                    author_id=1,
                    title="Guacamole",
                    subtitle="Creamy and delicious avocado dip",
                    date=date.today().strftime("%B %d, %Y"),
                    ingredients="Avocados, lime juice, onions, tomatoes, cilantro, salt.",
                    instructions="1. Mash avocados. 2. Mix with lime, onions, and tomatoes. 3. Serve chilled.",
                    img_url="https://www.allrecipes.com/thmb/6RyFPH5N4KKmZhNY0Giob_Jj3wc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-14231-guacamole-4x3-f7a3b5752c7f4f3fb934d03a8b548826.jpg"
                ),
            ]

            # Add the example posts to the session
            db.session.add_all(example_posts)
            db.session.commit()
            print("10 example recipes inserted into RecipePost table.")