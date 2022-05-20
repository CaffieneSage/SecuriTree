# SecuriTree                                                             by TheCaffieneSage 20/05/2022
Taking a look at binary tree data structures.

An Overview:

Super Secure Systems(S3) is a company specialising in physical security and access control management. Their product lines range from
simple door locks to more advanced mechanisms including cameras with facial recognition and motion control etc.
S3 require us to build an application, this application will provide a visual view of all the security hardware that has been implemented
at a given site. It will allow authorized operatives to access, monitor and control individual hardware elements at the site remotely, and
will implement a Tree Heirarchy based data structure.

Goals:

Securitree will (probably):
 * represent the relationships between security components visually as a tree structure.
 * Use said tree structure to navigate between nodes on the tree to lock and unlock doors on a premises.
 * Show the current state of all doors and security features on the site.
 * Provide a password or pincode based access method to prevent unauthorized access.
 * Store data in a text file (probably an encrypted one).

Technology:

The software should offer secure access to the sites security features, be easy to use for the end user, be reliable and as bug free as humanly
possible. To this end a graphical display should be used to make it obvious what the status of individual nodes of the tree are, and where the nodes are located
on site.
 I propose the use of python or similare language for easier prototyping, along with the use of a GUI module such as tkinter. Documentation is readily available 
 for this technology, easing the difficulty and reducing production time.
 
 To do list:
 
 *Implement a login page that accepts a username and password.
 *Create a main landing page with options to view the heirarchy, view the status of doors, or logout.
 *A page displaying the tree heirarchy in the system, showing how security features are interconnected.
 *A page with menus to control doors and features connected to the system.
 *Implement a file to store login data.
 *It may also be advantageous to implement some kind of logging system to track activity on site.

Alternatives:

*If a GUI proves too difficult to implement within a reasonable timeframe, a simpler command line
interface could be used instead. 
*A secure website could also be used to control systems remotely.

Testability and Monitoring:

 The codebase for a security system should be clean and self-documenting. Comments should be used sparingly, 
 but they should be present and to the point. In years to come the product needs to be maintanable, and
 possibly even extendable. The best way to achieve this is to keep best practices in mind. 
  

Links:
 * https://www.delftstack.com/howto/python/trees-in-python/
 * https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/
 * https://www.freecodecamp.org/news/how-to-write-a-good-software-design-document-66fcf019569c/
