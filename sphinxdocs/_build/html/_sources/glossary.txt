.. _glossary:

********
Glossary
********

.. glossary::

   administrator
      A special user created by default that has rights to configure and set access rights, so this user can create other users and set their access rights.

   advance product
      An artificial product created to be able to send advance invoices with a fixed amount (as opposed to a percentage). It is not really a product that you can buy or sell but it is used by the system to manage advance invoices. The advance invoice consists of just one invoice line with the advance product in quantity one and the advance amount as its price. When configuring the advance product make sure its type is 'service' and its supply method is 'produce'. Also you would set the income account of this product the account 'Advances from customers' received instead of the default 'Revenues' and remove the default tax on the product.

   analytic account
      A management account on which money amounts and quantities can be accumulated in parallel to financial accounts. Each entry into the financial ledger can also be associated with an analytic account allowing data to be analyzed in different ways as from financial accounts alone. It is also possible to make entries onto an analytic account without a counterpart entry into the financial accounts.

   analytic journal
      Just like financial account entries need to be recorded through a (financial) journal, so need analytic entries be made through a analytic journal. It provides a means of categorizing the entries. If a financial entry gives rise to an analytic entry, the analytic journal set on the financial journal will be used.
      
   anglo saxon accounting
      Can be set in the configuration of the accounting module. If set, the system recognizes the costs of goods sold when a sales invoice is confirmed when the :term:`inventory valuation method` is Perpetual (automatic) and for products of :term:`type <product type>` 'Stockable Product'. When a supplier invoice is received for stockable products, costs are not booked on the :term:`expense account` but the :term:`stock input account` (this account then reflects the 'goods to receive') is debited instead for the product costs as recorded on the product form and price differences are recorded on the :term:`price difference account`. When goods are received the stock valuation account is debited and the stock input account is credited. At time of confirming the sales invoice, apart from the account entries to record the accounts receivable and sales revenue, there will also be accounting entries made to record the costs of goods sold by debiting the :term:`expense account` and crediting the :term:`stock output account` for the costs of goods to be delivered. Finally, when goods are delivered the :term:`stock valuation account` is credited and the :term:`stock output account` is debited. 
      If anglo saxon accounting is not set the default :term:`continental accounting` applies.

   application
      An application or “app” is a special type of module that is more comprehensive in nature and has its own top level menu item which is an icon on the menu screen. Regular modules extend one of the applications.

   attribute
      see :term:`object`
      
   back order
      a :term:`transfer` created by the system for the part of the goods not available when validating a 'partially available' transfer. The back order can then be validated at a later stage when some or all of the goods of the back order become available

   bill of materials
      a bill of material (BOM) is an :term:`object` that specifies the components of a manufactured product or a :term:`kit` product. A BOM has at least one BOM line. A :term:`procurement` for a product with a Manufacture BOM (of the the type 'Manufacture this product') will create a :term:`Manufacturing Order` in case there is not enough stock to satisfy the procurement and the  action of the associated procurement rule is 'manufacture'. A procurement for a product with a Kit BOM (of type 'Ship this product as a set of components (kit)') never creates a manufacturing order but when a stock move is confirmed for such a product it will be exploded to all the individual products of its BOM lines. A Kit BOM is useful to group sets of components on a manufacture BOM so the manufacture BOM is easier to understand. It can also be used for selling kits to customers so the sales order remains simple with just one line per kit product but the delivery order is detailed listing all the individual products of the kit. 
      
   consumable
      see :term:`product type`   

   contact
      A person associated with a partner.
      
   continental accounting
      Under the default 'Continental' accounting system the costs of goods are recognized on the :term:`expense account` (often called  'Purchased Goods') when the vendor bill is confirmed and then corrected for goods received and shipped by indicating the same account as the :term:`stock input account` and the :term:`stock output account` (this account is often called the 'Inventory Variations'). 
      When a vendor bill is confirmed the value is debited  on the :term:`expense account` and accounts payable is credited. When stockable products are received and the :term:`inventory valuation method` is set to 'Perpetual (automatic)' accounting entries will made to debit the :term:`stock valuation account` and credit the  :term:`stock input account`. When goods are shipped the :term:`stock output account` is debited and the :term:`stock valuation account` is debited. When a customer invoice is confirmed no stock valuation entries are made or expenses recognized. The cost of goods sold at the end of the period is then difference between the 'Purchased Goods' and 'Inventory Variations' account.   

   company currency
      The currency of the financial statements of the company. Usually therefore the currency of the country the company is registered, so for PTS it is Chinese Yuan (CNY). The company currency is set on the company in Settings→Companies→Companies in the configuration tab of the company opened in form view. All accounting entries are in the company currency. If a different currency is used while making the entry then the amount is translated into the company currency at the most recent rate known to the system (the amount in foreign currency as well as the currency used is also stored with the entry).

   costing method
      The costing methods available can be configured in the purchasing module. Once configured as "Use a 'Fixed','Real' or 'Average' price costing method' on the product category the Costing Method field is visible and can be set to one of the following three values:
      
      * Standard: A fixed cost price is manually entered by the user on the product form (this is the default and also the method that always applies if the option 'Set a fixed cost price on each product' has been configured in the purchasing module).
      * Average: The cost price is an average price of all purchased goods and recomputed with each incoming shipment.
      * Real: The cost price displayed is the one of the last outgoing product. This should only be used with manufactured goods.

   customer lead time
      This is the time in number of days between confirming the sales order and the scheduling of the delivery order or the performance of the task. Is time within goods are delivered or services rendered you promised to customer. 

   database id
      Odoo automatically assigns to each record in the database a internal unique identification number called the database ID or simply the ID. The ID is a for the object (table) an unique integer number, which is used internally to refer to to the record. In the web client you can see the ID in the URL when a individual record is displayed, in the GTK client you can see the ID of a resource between brackets at the bottom of the page in form or list view.

   developer mode
      The developer mode can be activated in the dashboard screen of the Settings module to activate more advanced or technical functionality. The developer mode also shows technical data about the objects being accessed and is useful when debugging the system or looking up the internal names of the objects when say developing a new report. You can also perform certain operations like setting defaults, defining custom filters and so on normally not available.

   domain
      An expression specifying a subset of records of an active set. It works like a search 'filter'. Only records that match the filter are selected to be part of the subset. The difference is that domains are set in actions or on fields and cannot be changed in the view itself whereas search filters can be changed.

   expense account
      A :term:`property field` that can be set both on the product and the product category. Normally this account is debited when a vendor bill for this product is confirmed at the cost price in the product form. It should therefore point to some expense account. If not set the default debit account of the journal of the vendor bill is used.
      Under the :term:`anglo saxon accounting` system, for Stockable Products, however, not this account is debited, but instead the :term:`stock input account` (normally 'Goods to Receive') is debited. 
      Also only for Stockable Products and under the Anglo Saxon system AND when Perpetual accounting is used, the expense account is debited for the costs of the goods when confirming a sales invoice so for these products the expense account should be the 'Cost of Goods Sold' account. 
 
   fiscal position
      The applicable tax rates (like VAT) for buying and selling are set on the product. However, for some partners other rates might apply (for example if they are abroad). A fiscal position is a set of rules that specify how to override taxes set on the product. Once defined, a fiscal position is set on the partner which will then serve as the default fiscal position on purchase or sales orders involving this partner.

   income account
      A :term:`property field` that can be set both on the product and the product category.
      This account is credited when a customer invoice for this product is confirmed at the sales price of the invoice. It should therefore point to a revenue financial account like 'Sales'. If not set the default credit account of the journal is used when creating a customer invoice. The field must have been set, however, to be able to create an invoice from the sales order.
      
   inventory valuation method
      Set on the product category form, this field determines whether the system makes automatic journal entries for stock moves or not. 
      If it is set to 'Periodic (manual)' no automatic journal entries are made. Instead, the accountant should make manual entries at the end of each period to properly reflect the value of goods in stock.
      If set to 'Perpetual (automatic)' the system will make automatic journal entries as follows. Whenever goods are moved into stock, the :term:`Stock Valuation Account <stock valuation account>` is debited for the value of the goods calculated using the cost price on the product (which in turn is determined by the :term:`costing method` in force for the product). The :term:`Stock Input Account` is credited for the same value.

   invoicing policy
      The invoicing policy determines when the invoice from the sales order can be generated. It is set on the product.
      There are 2 options:
      
      #. On ordered quantities: the invoice is based on the quantities the customer ordered. 
      #. On delivered quantities: the invoice is based on the quanties the vendor delivered (time or deliveries).

   kit
      A kit is a product that represents a set of components that are delivered without being first assembled or mixed (so their is no actual manufacturing operation performed). For a product to be a kit, it must have Kit :term:`bill of materials` of type 'Ship this product as a set of components (kit)'. 
      
   manufacturing order
      An :term:`object` that represents an instruction to to produce a number of products using a specific bill of material with a start deadline. The manufacturing order contains prepopulated stock move lines (calculated on the basis of the bill of materials) to bring in the needed materials from stock and move the finished proucts to stock. Starting production moves the materials to the :term:`stock location` production while finishing the order moves the finished product into stock. 
      
   manufacturing lead time
      This is time is set on the product and signifies the average time it takes to produce the product provided that all the components and subassemblies of its :term:`bill of materials` are available.    

   model
      see :term:`object`

   module
      A unit of functionality in the system. Odoo is a very modular system meaning that it has only very basic core functionality while you add the functionality required by adding modules. Modules contain programming code, view and report definitions and other data.

   object
      An object is a container of data and logic to manipulate the data. It represents a thing, a process, event, transaction or rule important to keep track of to support the business processes or internally for the management of the information system itself. Examples are products, work-flows, sales orders, purchase orders, payment, users, security rules etc. The term object can sometimes refer to the object class (e.g. the concept 'Purchase Order') or a particular instance of that object class (eg. PO0019 to supplier 'InfoTech') . In Odoo the object class is mostly referred to as 'model' but sometimes just as 'object' while a particular instance is referred to as 'resource' or 'record'. A 'model' consists of 'fields' which are attributes of the object we want to keep track of and 'methods' which consist of logic to manipulate the values of those fields. In database terms, loosely, an object would be represented by a table and an object instance by a record or row in the table, a field would be a column of the table and the value of the field the intersections of the column and the row. The models are defined in the programming code of the Odoo modules while the resources are represented in the database.

   partner
      A company or person the company has relations with. Can be a client, supplier, government agency, employee etc. If a partner is a company it can have 'children'. The children cannot be companies but must be contacts or addresses of the company.
      
   picking
      see :term:`transfer`
      
   price difference account   
      A :term:`property field` that can be set both on the product and the product category. It is used when the :term:`anglo saxon accounting` system is adopted, only for stockable products with the :term:`inventory valuation method` set to 'Perpetual (automatic)'. The account will automatically record differences between the invoiced purchase price and the cost price as recorded on the product form when confirming the vendor bill. It is only used under anglo saxon system since costs of stockable products are under that only recognized when selling these products but costs due to variations in prices can so be recognized immediately. In the continental system this is alreay built in as costs are already recognized when purchasing goods. It can be relevant even when costing method is 'average' when there is a discrepancy between the invoice costs and the purchase order costs since stock valuation is done according to the purchase order prices and not the invoice prices.
           

   price list
      A set of rules to determine the sales price or purchase prices on sales order lines or purchase order lines depending on whether its type is 'sale' or 'purchase'. A price list has one currency and is associated with one or more price list versions of which one can only be applicable at any time (as determined by the start and end date). Each price list version has a set of price list items which are the actual rules to calculate the prices.

   procurement
      A procurement is an internal object that holds data about when a certain quantity of a product is needed at what location. Based on procurements the system can generate purchasing orders, manufacturing orders, stock moves to fulfill the needs. The procurement also links to documents generated to fulfill the need.

   project
      A project is a set of tasks. A project is generated from a confirmed sales order.

   product template
      The product template is an object describing the common attributes of a certain type of product. A product template resource can be linked to one or more product variant resources that share the values for the common attributes of the template resource but have different values for variant attributes. For a product template to have more than one variant there must also be at least one user defined attribute. The user defined attributes are usually concepts like color, size and so on. Each variant belonging to the same template will then have a different values for the user defined attributes.   

   product type
      Odoo distinguishes between three product types, set on the product form:
      
      #. Stockable product: normal physical product that can be stocked.
      #. Consumable: only relevant in a production oriented enterprise. The system assumes there is always enough stock of this product. In other words it will always  flag stock moves of this product as 'available'. There is also no automatic inventory accounting for consumables. Sellable products should not have the consumable product type. 
      #. Service: a product that is not physical. You cannot keep stock of a service and it cannot appear in stock moves. Services can be bought and sold or produced by the company. 

   product variant
      See :term:`product template`
   
   property field
      A special type of field also called 'configuration parameter or company specific field'. Can be set in the view of a particular resource (like the product form view) or at Settings→Technical→Parameters→Configuration Parameters.
      The purpose of a property field is twofold:     
      
      #. The property can have a different value for each company in the system. Depending on which company the user is logged in as, the property field of the same resource has or can have a different value. This allows you to share resources between companies but still let the property fields differ.
      #. Allows setting different levels of defaults for fields. If the property field for a particular resource is not set the system will then check if there is a 'Generic' value for the company the user is logged in for that field which is not bound to a paricular resource. If that is not found as well the system will check there is a 'Generic' value for the property field for the system as a whole which is also not bound to a company. 'Generic' properties can only be set in the Settings module (Settings→Technical→Parameters→Company properties).
      
      Note that you should never set 'Generic' values for the product level property fields that have corresponding product category property fields as this will result in the product category properties being ignored.

   pull rule
      A pull rule or procurement rule is rule that specfies how a :term:`procurement` at a certain location should be fulfilled. There are three ways: 'buy' (generate purchase order), 'manufacture' (generate manufacturing order), or 'move from another location' (generate stock move) from another location to this location. 

   push rule
      A push rule is a rule that specifies that when a products arrives at a certain :term:`stock location` a new :term:`transfer` should be prepared automatically to another location. For example if a company has a test location for incoming goods you could specify that all products arriving at the "Input" location for the company should have a transfer prepared to the "test" location and all products to the "test" location should have a transfer prepared to the "stock" location for the default case that products are tested OK. The advantage is that operator can simply validate the prepared transfer instead of having to enter all data herself. 

   Python
      A popular, general-purpose, high-level, cross-platform, interpreted programming language whose philosophy focuses mainly on code readability and maintainability. Designed by a Dutch guy: Guido van Rossum.

   record
      see :term:`object`
      
   reordering rule
      A reordering rule, when set on a product, determines if the system should create a new :term:`procurement` to replenish stock levels of that product on a a certain :term:`stock location' when the 'Run Reordering Rules' :term:`method <object>` is run.   

   resource
      see :term:`object`

   route
      A route is a defined path goods take through the system determined by :term:`Push Rules <push rule>` and/or :term:`Pull Rules <pull rule>`. Routes are configured under Warehouse→Configuration→Routes (when advanced routing is ON). Several are predefined by the modules installed like 'Buy' (purchase module - a draft purchase order is generated), 'Make to Order' (stock module - a procurement is created irrespective of stock level), 'Drop Shipping' (dropship module - defines a route from vendor to customer directly), 'Ship Only' (is make-to-stock, goods are taken from stock while no procurement is generated - the procurements are generated when running the Run Reorder Rules wizard). Routes can be applicable to :term:`Warehouses <warehouse>`, Individual Products, Product Categories, or Sale order lines. In effect it determines the :term:`stock moves <stock move>` and :term:`transfers <transfer>` that are generated by the system when fulfilling a procurement. The system chooses a route and selects an procurement rule from the route when processing a procurement that has no procurement rule yet. It will select the rule matching the procurement location with the highest route sequence and then with the highest rule sequence in the following order of precedence:
      
      #. From the route ids on the procurement (if explicitly set by user)
      #. From the products and product categories to which products belongs
      #. From the warehouse to which procurement belongs
      #. From global procurement rules (those that have no route specified)

   resource
      see :term:`object`
      
   scheduled actions
      Accessible under Settings→Technical→Automation/Scheduled Actions when the :term:`developer mode` has been activated. It schedules triggering certain methods of :term:`objects <object>` at regular intervals. 
      
   stock input account
      Set on the product category in a :term:`property field`, this account is credited for the corresponding value when goods are entered into stock and the :term:`inventory valuation method` on the product category has been set to 'Perpetual (automated)'. The value is calculated as the mathematical product of the quantity moved into stock and the cost price on the product form. Under :term:`anglo saxon accounting`, when confirming a vendor bill and for stockable products this account is debited  instead of the :term:`expense account` as counterpart for accounts payable (irrespective of inventory valuation method).
      
   stock location
      A stock location can act as the source or destination of a term:`stock move`. It hold data used in accounting and logistics. A location has a stock level for each good calculated by the difference between outgoing and incoming stock moves. Stock locations can be grouped and put in hierarchies. Every company has at least one group of such locations: the :term:`warehouse`.
      It can be of different types:
      
      * Internal: a real physical location in the company where goods are stored
      * Customer: a 'sink' to where sold products go to
      * Vendor: a 'source' from which purchased products come
      * Transit: a location for administrative use that acts as a buffer between own companies
      * Inventory Loss: a 'virtual' location that acts as the destination for lost goods.
      * Production: a 'virtual' location that acts as the destination for components and raw materials and the source for finished goods or sub-assemblies.
      
   stock output account
      Set on the product category in a :term:`property field`, this account is debited for the corresponding value when goods are moved out of stock and the :term:`inventory valuation method` on the product category has been set to 'Perpetual (automated)'. The value is calculated as the mathematical product of the quantity moved out of stock and the cost price on the product form.  Under :term:`anglo saxon accounting`, when confirming a sales invoice, for stockable products and when the :term:`inventory valuation method` is set to 'Perpetual (automatic)' this account is automatically credited (and the :term:`expense account` Costs of Goods Sold is debited) so the account should point to 'Deliveries'.        
      
   stock move
      A stock move is an term:`object` that holds captures data about the physical movement of a good. Based on 'confirmed' or 'validated' stock moves the future or current stock level is calculated at a particular term:`stock location`  
    
   stock valuation account
      Set on the product category in a :term:`property field`, this account is debited for the corresponding value when goods are moved into stock and the :term:`inventory valuation method` on the product category has been set to 'Perpetual (automated)' and credited when goods are moved out of stock. The stock valuation account thus reflects the value of goods in stock.

   task
      A task is an assignment within a project. A task is assigned to one person. A task can go through various stages.

   tax
      In Odoo you can define taxes that applicable to buying and selling (usually VAT taxes). Once defined the system will calculate the taxes on a purchase (order) or on a sale (order), and will automatically make the tax entries in the ledger and or accumulate the taxes for tax reporting purposes.

   toggle button
      A button that can be in two states 'on' and 'off'. 'On' or 'active' is represented by a button that is in a pressed down state and is darker shade. 'Off' or 'inactive' is represented by showing the button in released state and lighter shade. The toggle button is used in search views to search on boolean fields that can have a True or False value. Like for example the 'Is Customer?' field.
      
   transfer
      A transfer is a group of term:`stock moves <stock move>` with the same source and destination location and that are processed at the same time. A transfer can be in different states depending on the state of the stock move: 
      
      * draft: all stock moves are in draft state so there is no influence on stock levels.
      * waiting availability: all the goods are not available at the source location so transfer cannot be 'validated'.
      * partially available: some of the goods are not available at the source location some are. The transfer can only be validated for a part of the goods for the other part a :term:`back order` will be created.
      * available: all goods are available at the source location. The transfer can be validated in full.
      * done: the transfer has been 'validated' so the current stock level at the source location has fallen while the stock levels at the destination location.
      
      Transfers are named differently according to role:
      
      * Receipts: transfers from suppliers to the company. They are always available as availability is not something within company's control. They are validated the moment the goods arrive at company. Receipts are generated and associated with a purchase order.
      * Deliveries: transfers from company to customer. Generated and associated with a sales order.
      * Internal: transfers between :term:`stock locations <stock location>` inside the company.
      * Manufacturing: transfers generated and associated with a manufacturing order: from stock to the production location for components and raw materials and from production to stock for finished products (or sub-assemblies).
      
   unit of measure
      The standard of measure (UoM) in which the quantity of a product is expressed. The unit of measure belongs to a category. Quantities expressed in one UoM can also be expressed in another UoM as long as both these UoMs belong to the same category. If both UoMs are not of the same type the system will raise an error if such conversion is attempted. Each UoM type has one 'reference' UoM. The other UoMs of the same type must carry a factor relative to the reference UoM, so UoMs can be converted.

   view
      A type of screen used to present data to the user, or more precisely to present (the resources of) an object to the user. These are different types of views:
      
      * list or search view: data is presented in rows, with one record per row
      * form view: data is presented as form with one record per screen or window. The form view can contain list or form views of related records
      * graph view: data is presented in a graph
      * dashboard view: a combination of list, form and graph views. In the web client often activated as first view when activating the module. In the GTK client the dashboard is usually available under the reporting menu item. 
      * gantt view: data is presented in the form a gantt chart, that is bars on a calendar. Useful if the object has a duration.
      * calendar view: data is presented on a calendar type (only useful if there is a date field in the records to display)
      * kan ban view: data is presented as if on a black board
      * diagram view: data is presented in a diagram also allowing editing of diagram (adding edges and nodes). Only applicable to presenting or editing workflows and only availabe in the web client (under Administration→Customization→Workflows).     
      
      The object or objects to display must support the views before you can use them. List and form views are always supported.
      
   warehouse
      A warehouse is a top level group of :term:`stock locations <stock location>` associated with a company consisting of an 'input', 'stock' and 'output' location. The company stock level is calculated from the goods in stock location.
      
   wizard
      A feature of a software package that automates complex tasks by asking the user a series of easy-to-answer questions.


