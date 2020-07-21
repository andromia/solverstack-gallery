// Adds a header row to the table and returns the set of columns.
// Need to do union of keys from all records as some records may not contain
// all records.

function onlyUnique(value, index, self) { 
  return self.indexOf(value) === index;
}

function buildVrpMap(data) {

    console.log("data", data)

    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });
    }

    var pallets = unpack(data, "pallets"),
        lat = unpack(data, "latitude"),
        lon = unpack(data, "longitude"),
        cluster = unpack(data, "cluster"),
        vehicle = unpack(data, "vehicle_id"),
        stop_num = unpack(data, "stop_num")
        size = [],
        hoverText = [],
        //scale = 2.* Math.max(null, pallets) / (100**2);
        scale = 2;
}
