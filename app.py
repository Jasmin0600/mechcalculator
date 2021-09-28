from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():

    min_range = 25
    max_range = 127
    val1 = 1.5
    val2 = 25.4
    module = int(request.form.get("module"))
    start = int(request.form.get("start"))

    lead = round(3.1416 * module * start, 5)
    print("lead : ", lead)

    extra_multi = request.form.get("multi")

    def number_of_digits_post_decimal(x):
        count = 0
        residue = x - int(x)
        if residue != 0:
            multiplier = 1
            while not (x * multiplier).is_integer():
                count += 1
                multiplier = 10 * multiplier
            return count
    num_post_decimal = number_of_digits_post_decimal(lead)

    if (num_post_decimal <= 5):
        accuracy = num_post_decimal
    else:
        accuracy = 5

    list1 = []

    if(extra_multi=="with_multi"):
        for a in range(min_range, max_range):
            for b in range(min_range, max_range):
                for c in range(min_range, max_range):
                    for d in range(min_range, max_range):
                        # print("((",a,"/",b,")*(",c,"/",d,"))",sep='')
                        our_value = ((((a / b) * (c / d)) * val1) * val2)
                        our_value = round(our_value, accuracy)
                        if (our_value == lead):
                            #print("(", a, "/", b, ")*(", c, "/", d, ")", sep='')
                            abcd = a, b, c, d
                            list1.append(abcd)

    else:
        for a in range(min_range, max_range):
            for b in range(min_range, max_range):
                for c in range(min_range, max_range):
                    for d in range(min_range, max_range):
                        # print("((",a,"/",b,")*(",c,"/",d,"))",sep='')
                        our_value = ((a / b) * (c / d))
                        our_value = round(our_value, accuracy)
                        if (our_value == lead):
                            #print("(", a, "/", b, ")*(", c, "/", d, ")", sep='')
                            abcd = a, b, c, d
                            list1.append(abcd)


    # python code end
    return render_template('index.html', jasmin=list1)

if __name__ == "__main__":
    app.run(debug=True)