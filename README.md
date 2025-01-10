# EcommerceCart_Team8

Welcome to the **Cart System Project**! This project is a user-friendly eCommerce cart system designed to enhance the online shopping experience. With its intuitive interface and efficient backend, it offers seamless navigation from product selection to checkout.

---

## **Project Flow**
1. **Login Page** → **Main Page** → **Electronics/Clothing/Groceries** → **View Cart** → **Checkout**
2. The first three steps have been successfully implemented.

---

## **Project Summary**
The **Cart System** is a simple yet powerful eCommerce solution that allows users to:
- Add products to their cart.
- View and manage cart contents.
- Update product quantities.
- Remove items.
- Proceed to an easy and secure checkout process.

The cart data is securely stored in a JSON-based structure, ensuring that users’ carts are retained even after exiting the application.

---

## **Key Features**
- **Add to Cart**: Add multiple items effortlessly.
- **Update Quantity**: Modify item quantities on the fly.
- **Remove Items**: Delete unwanted products with ease.
- **View Cart**: Check detailed product information (name, price, quantity).
- **Data Backup**: User carts are saved as nested dictionaries in a JSON database, e.g.,
  ```
  {
    "<username>": {
      "<product1>": {"quantity": q1, "price": p1},
      "<product2>": {"quantity": q2, "price": p2}
    }
  }
  ```

---

## **Steps to Use**
1. **Login/Signup**:
   - Enter your credentials on the login page.
   - If new, use the signup option to create an account.

2. **Main Page**:
   - Choose from three categories: Electronics, Clothing, Groceries.

3. **Category Pages**:
   - **Electronics**:
     - Add/remove items using the `+`/`-` buttons.
     - View warranty details for each product.
   - **Clothing**:
     - Add/remove items using the `+`/`-` buttons.
     - Select color and size using dropdown menus.
   - **Groceries**:
     - Add/remove items using the `+`/`-` buttons.
     - Check expiry dates for products.

   > **Note**: The total price is updated dynamically and displayed at the bottom right of the screen.

4. **Cart & Checkout**:
   - Review and modify your cart.
   - Proceed to payment by selecting a payment method (UPI, Card, or Net Banking).

5. **Payment**:
   - Complete the payment to finalize your order.

---

## **Libraries Used**
1. **json**: For storing and managing user data.
2. **tkinter** and **customtkinter**: For building an interactive GUI.
3. **warnings**: Implicitly used by customtkinter for handling alerts.
4. **os**: (If applicable) For managing file paths or external resources.

---

## **Work Division**
- **Login Page & Main Page**: Shashank
- **Checkout Page & Cart Page**: Yash Sultania
- **Groceries, Clothing & Electronics Pages**: Hasini
- **Payment Page**: Abhinav

---

## **Team Members**
- **K V Shashank Pai** - BT2024250
- **Yash Sultania** - BT2024013
- **Ravi Abhinav** - BT2024239
- **Hasini Yamsani** - BT2024133

---

Thank you for exploring our Cart System Project. We’re excited to bring this idea to life and look forward to your feedback!

