def get_rating(prompt):
    """Get a valid rating from 1 to 5 with input validation."""
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # Define aspects and table structure
    aspects = [
        "pay",
        "Time till starting to earn money",
        "How many regions can you study in",
        "passion",
        "a level subjects difficulty",
        "scholarship ease",
        "price of education (college)",
        "prestige",
        "difficulty & stress",
        "work stress",
        "salary growth over time",
        "Love of work (aka purposeful)",
        "fun work"  # Added as per requirement #4
    ]
    
    # Create 2D array with header
    data = [
        ["Aspect", "importance", "engineer", "doctor", 
         "productengineer", "productdoctor"]
    ]
    
    # Collect user input and calculate products
    for aspect in aspects:
        print(f"\nEvaluating: {aspect}")
        imp = get_rating("Importance (1-5 where 5 is most important): ")
        eng = get_rating("Engineer satisfaction (1-5 where 5 is best): ")
        doc = get_rating("Doctor satisfaction (1-5 where 5 is best): ")
        
        # Calculate products
        prod_eng = imp * eng
        prod_doc = imp * doc
        
        # Double the product for 'fun work' aspect
        if aspect == "fun work":
            prod_eng *= 2
            prod_doc *= 2
            
        # Add row to data table
        data.append([aspect, imp, eng, doc, prod_eng, prod_doc])
    
    # Calculate totals
    total_eng = sum(row[4] for row in data[1:])  # Skip header
    total_doc = sum(row[5] for row in data[1:])  # Skip header
    
    # Display results and recommendation
    print("\n" + "=" * 50)
    print(f"Total score for Engineer: {total_eng}")
    print(f"Total score for Doctor: {total_doc}")
    print("=" * 50)
    
    if total_eng > total_doc:
        print("You will be better off choosing to become an Engineer")
    elif total_doc > total_eng:
        print("You will be better off choosing to become a Doctor")
    else:
        print("Both careers are equally suitable for you")

if __name__ == "__main__":
    main()