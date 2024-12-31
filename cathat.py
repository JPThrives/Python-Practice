def cat_hat(str):
    cat_count = str.count("cat")
    hat_count = str.count("hat")

    return cat_count == hat_count

print(cat_hat("cat"))