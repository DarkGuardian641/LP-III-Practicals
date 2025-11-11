# 🧾 Business Network and Alternatives for Hyperledger Composer

## ⚠️ Important Notice

IBM shut down the **Composer Playground demo** hosted on **Bluemix (IBM Cloud)** around **mid-2020**, and **Hyperledger Composer itself is now deprecated**.  
However, you still have **three working alternatives** to **run or demonstrate a Hyperledger business network locally or via modern replacements** 👇

---


## 🧩 Option 1: Run Hyperledger Composer Locally (Offline Playground)

### 🧠 What it is
You can still install **Hyperledger Composer Playground** locally using Node.js and run it on your system (no IBM Cloud needed).

---

### 🧰 Installation Steps

```bash
# 1. Install Node.js (v8.x or v10.x compatible)
#    Download from: https://nodejs.org/en/download/

# 2. Install Hyperledger Composer CLI and Playground
npm install -g composer-cli
npm install -g composer-playground

# 3. Start local Playground
composer-playground
```

Open your browser and visit:
```
http://localhost:8080
```

---

### 🚀 To Deploy Your Business Network

1. Prepare your `.bna` file (e.g., `supplychain-network.bna`)
2. Open **Playground** → click **Deploy a new business network**
3. Upload your `.bna` file
4. Once deployed, click **Test**
5. Add participants, assets, and transactions to simulate flow

---

### 🧩 To Generate a `.bna` File from Source Code

If your folder contains:
```
models/
lib/
permissions.acl
queries.qry
package.json
```
Run this command:
```bash
composer archive create -t dir -n .
```
It will create:  
`supplychain-network@0.0.1.bna`

---

## 🧩 Option 2: Use Hyperledger Fabric (Composer Replacement)

Since Composer is deprecated, new blockchain logic is written **directly on Hyperledger Fabric** using:

- **Chaincode (Smart Contracts)** in **Go**, **Java**, or **Node.js**
- **Fabric CA** for identity management
- **Fabric SDK** for integration

👉 Learn more: [https://hyperledger-fabric.readthedocs.io/](https://hyperledger-fabric.readthedocs.io/)

You can recreate your same **Supply Chain** logic using Fabric’s peer network.

---

![Hyperledger Fabric Replacement Section](file_0000000074487209a388c430bb68b60e)

---

## 🧩 Option 3: Use a Modern Web Sandbox Alternative

If you only need a **visual blockchain demo**, try:

- **IBM Blockchain Platform Extension for VS Code**  
  → Download: [https://marketplace.visualstudio.com/items?itemName=IBMBlockchain.ibm-blockchain-platform](https://marketplace.visualstudio.com/items?itemName=IBMBlockchain.ibm-blockchain-platform)

It provides an integrated **Playground-like UI** for creating and testing networks locally.

---

## ✅ Summary Table

| Purpose | Recommended Option | Description |
|----------|--------------------|-------------|
| Academic / College Project | Run Composer Playground locally | Simple to demonstrate |
| Enterprise Development | Hyperledger Fabric SDK | Production-grade system |
| Visual Demo / Prototype | IBM Blockchain Platform (VS Code) | GUI-based local testing |

---

# 💼 Business Program: Supply Chain Network using Hyperledger Composer

## 1. Network Name
```
supplychain-network
```

---

## 2. Model File (`models/org.example.supplychain.cto`)
```javascript
/**
 * Supply Chain Business Network Model
 * Namespace: org.example.supplychain
 */

namespace org.example.supplychain

// Participants
participant Supplier identified by supplierId {
  o String supplierId
  o String name
  o String location
}

participant Retailer identified by retailerId {
  o String retailerId
  o String name
  o String location
}

// Asset
asset Product identified by productId {
  o String productId
  o String name
  o String category
  o Double price
  --> Supplier owner
}

// Transaction
transaction TransferProduct {
  --> Product product
  --> Retailer newOwner
}

// Event
event ProductTransferred {
  o String productId
  o String oldOwner
  o String newOwner
}
```

---

## 3. Script File (`lib/logic.js`)
```javascript
/**
 * Business Logic for Supply Chain Network
 * @param {org.example.supplychain.TransferProduct} tx
 * @transaction
 */
async function TransferProduct(tx) {
    const product = tx.product;
    const oldOwner = product.owner.name;
    const newOwner = tx.newOwner;

    // Update ownership
    product.owner = newOwner;

    // Update the asset registry
    const productRegistry = await getAssetRegistry('org.example.supplychain.Product');
    await productRegistry.update(product);

    // Emit an event for the transfer
    const event = getFactory().newEvent('org.example.supplychain', 'ProductTransferred');
    event.productId = product.productId;
    event.oldOwner = oldOwner;
    event.newOwner = newOwner.name;
    emit(event);
}
```

---

## 4. Permissions File (`permissions.acl`)
```javascript
/**
 * Access control rules for Supply Chain Network
 */
rule DefaultAllowAll {
  description: "Allow all participants to read all resources"
  participant: "ANY"
  operation: READ
  resource: "org.example.supplychain.*"
  action: ALLOW
}

rule SupplierWriteAccess {
  description: "Allow suppliers to create and update their own products"
  participant(p): "org.example.supplychain.Supplier"
  operation: CREATE, UPDATE
  resource(r): "org.example.supplychain.Product"
  condition: (r.owner.getIdentifier() == p.getIdentifier())
  action: ALLOW
}

rule RetailerReadAccess {
  description: "Allow retailers to read all products"
  participant: "org.example.supplychain.Retailer"
  operation: READ
  resource: "org.example.supplychain.Product"
  action: ALLOW
}
```

---

## 5. Queries File (`queries.qry`)
```javascript
/**
 * Example query file
 */
query SelectAllProducts {
  description: "Return all products in the network"
  statement:
    SELECT org.example.supplychain.Product
}

query SelectProductsBySupplier {
  description: "Return products owned by a specific supplier"
  statement:
    SELECT org.example.supplychain.Product
      WHERE (owner == _$supplier)
}
```

---

## 6. Test Data (Sample JSON for Playground)
```json
{
  "Supplier": [
    {
      "$class": "org.example.supplychain.Supplier",
      "supplierId": "SUP1",
      "name": "Alpha Supplies",
      "location": "Mumbai"
    }
  ],
  "Retailer": [
    {
      "$class": "org.example.supplychain.Retailer",
      "retailerId": "RET1",
      "name": "Beta Retail",
      "location": "Pune"
    }
  ],
  "Product": [
    {
      "$class": "org.example.supplychain.Product",
      "productId": "PROD1",
      "name": "Smartphone",
      "category": "Electronics",
      "price": 25000,
      "owner": "resource:org.example.supplychain.Supplier#SUP1"
    }
  ]
}
```

---

## 7. Execution Steps in Composer Playground

> ⚠️ The original IBM-hosted playground is offline.  
> Use the **local setup** (`composer-playground`) or **VS Code extension**.

1. Open local Composer Playground → [http://localhost:8080](http://localhost:8080)
2. Click **Deploy a new business network** → Enter `supplychain-network`
3. Upload:
   - `models/org.example.supplychain.cto`
   - `lib/logic.js`
   - `permissions.acl`
   - `queries.qry`
4. Click **Deploy**
5. Under “Test” tab:
   - Add participants (Suppliers, Retailers)
   - Add assets (Products)
   - Run **TransferProduct** transaction
6. Observe **ProductTransferred** event and new ownership.

---

## 8. Output (Expected)
- Ownership of product changes from Supplier → Retailer  
- `ProductTransferred` event emitted  
- Queries reflect updated ownership

---

## 9. Conclusion
This **Supply Chain Business Network** demonstrates blockchain transparency and traceability using **Hyperledger Composer**.  
It models secure transfer of ownership and can extend to **food safety**, **logistics**, or **pharmaceutical tracking**.

---

## 🔗 Documentation
Composer Playground Docs (archived):  
[https://hyperledger.github.io/composer/v0.19/playground/playground-index](https://hyperledger.github.io/composer/v0.19/playground/playground-index)

---

