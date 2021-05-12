/**
 * Render a map.
 * @param {*} mapElementId the id of the map control (typically an HTML div)
 * @param {*} tileSource source of map tiles
 * @param {*} attribution map attribution
 * @param {*} centreCoordinates the center coordinate of the map view (format: [x, y])
 * @param {*} zoomLevel starting zoom level of the map
 * @param {*} data the json data for adding layers to the map
 * @param {*} layerFn function(mapId, data) that is applied to the data to add layers to the map
 */
 // eslint-disable-next-line max-params, no-unused-vars
 function renderMap(mapElementId, data, layerFn, {tileSource, attribution, centreCoordinates, zoomLevel} = {}) {
	const tileSrc = tileSource || 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	const attrib = attribution || '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>';
	const centre = centreCoordinates || [54.1401465, -101.0847617];
	const zoom = zoomLevel || 4;

	const tileProperties = {
		attribution: attrib,
		subdomains: ['a', 'b', 'c']
	};
	const tileLayer = L.tileLayer(tileSrc, tileProperties);
	const myMap = L.map(mapElementId, {
		scrollWheelZoom: true
	});

	tileLayer.addTo(myMap);
	myMap.setView(centre, zoom);
	layerFn(myMap, data);

	return myMap;
}

function createClusterIcon(cluster) {
	return L.divIcon({
		html: '<div class="cluster-count">' + cluster.getChildCount() + '</div>',
		className: 'default-cluster-icon',
		iconSize: new L.Point(30, 30)
	});
}

function addEventMapLayers(myMap, events, markerClickListener) {
	const markerIcon = L.icon({
		iconUrl: '/static/images/leaflet/marker-icon.png',
		iconSize: [25, 41]
	});

	const markers = L.markerClusterGroup({
		showCoverageOnHover: false,
		iconCreateFunction: createClusterIcon
	});

	events.forEach((evnt) => {
		let marker = L.marker([evnt.latitude, evnt.longitude], {icon: markerIcon});

		const tooltip = `${evnt.name}`;

		const popupHtml = `
			<div class='marker-popup'>
				<h5 class="text-center">${evnt.name}</h5>
			</div>
		`;
		marker.bindTooltip(tooltip);
		// marker.bindPopup(popupHtml);

		marker.on('click', (e) => {
			markerClickListener({
				name: evnt.name,
				latitude: evnt.latitude,
				longitude: evnt.longitude
			});
		});

		markers.addLayer(marker);
	});

	myMap.addLayer(markers);
}
