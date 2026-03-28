
## [Excessive trust in client-side controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls)

- Check if adding an item to the cart has a price parameter
- Change it to $0 and send the request to get a free item

## [High-level logic vulnerability](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level)

- Check if there is a quantity parameter in the POST /cart request. 
- Change the quantity to a negative number. This will make the price of the items in your cart go to negative as well.
- Add a new item to the cart. The total amount should go over $0 but should be under the store credit amount.
- Place the order to get a free item.

## [Inconsistent security controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-security-controls)

- Try to access the /admin panel. You should get an error that only DOntWannaCry users all allowed to access the panel.
- Create an account and change the email address to one with @dontwannacry.com
- You should now have access to the admin panel


## [Flawed enforcement of business rules](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-flawed-enforcement-of-business-rules)

- Log in to get the coupon code.
- Sign up for new letter to get a second coupon code.
- You can add the codes more than once if you alternate them.
- Reuse the two codes until the item is lower than your remaining store credit.


## [Low-level logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-low-level)




## [Inconsistent handling of exceptional input](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-handling-of-exceptional-input)


## [Weak isolation on dual-use endpoint](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint)


## [Insufficient workflow validation](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-insufficient-workflow-validation)


## [Authentication bypass via flawed state machine](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine)


## [Infinite money logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money)


## [Authentication bypass via encryption oracle](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-encryption-oracle)


