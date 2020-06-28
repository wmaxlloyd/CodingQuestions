// CONVERT:

const input = {
  "data": {
    "0000": {
        "type": "Integer",
        "name": "happiness",
        "data": "10"
   },
    "0001": {
        "type": "String",
        "name": "Why?",
        "data": "because"
    },
    "0002": {
        "type": "NestedObject",
        "data": {
             "0000": {
                  "type": "String",
                  "name": "NPSGroup"
              },
             "0001": {
                  "type": "Integer",
                  "name": "NPSScore"
             },
             "0003": {
                "type": "NestedObject",
                "data": {
                     "0004": {
                          "type": "String",
                          "name": "NPSGroup"
                      },
                     "0005": {
                          "type": "Integer",
                          "name": "NPSScore"
                     }
                }
            }
        }
    }
 }
}
// TO:

// {
//  "dataView":
//  [
//      {
//         "type": "Integer",
//         "name": "happiness",
//         "data": "10",
//         "id": "0000"
//      },
//      {
//            "name": "Why?",
//            "data": "because"
//            "type": "String"
//            "id": "0001"
//      },
//      {
//            "id": "0002",
//            "type": "NestedObject",
//            "data": [
//                   {
//                        "id": "0000",
//                        "type": "String",
//                        "name": "NPSGroup"
//                   },
//                   {
//                        "id": "0001",
//                        "type": "Integer",
//                        "name": "NPSScore"
//                   }
//            ]
//      }
//   ]
// }

const convertJson = (input) => {
    const convertedJson = {
        dataView: []
    }
    Object.keys(input.data).forEach(key => {
        const keyData = input.data[key]
        const dataView = Object.assign({id: key}, keyData)
        if (keyData.type == "NestedObject") {
            convertedNestedData = convertJson({
                data: keyData.data
            })
            dataView.data = convertedNestedData.dataView
        }
        convertedJson.dataView.push(dataView)
    })
    return convertedJson
}

console.log(JSON.stringify(convertJson(input), null, 2))