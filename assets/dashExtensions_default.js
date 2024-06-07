window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, context) {
            const {
                min,
                max,
                colorscale,
                style,
                colorProp
            } = context.hideout; // get props from hideout
            const csc = chroma.scale(colorscale).domain([min, max]); // chroma lib to construct colorscale
            const mycolor = csc(feature.properties[colorProp]);
            style.fillColor = mycolor; // set color based on color prop
            style.color = mycolor; // set color based on color prop
            style.weight = 0.9; // set color based on color prop
            return style;
        },
        function1: function(feature, latlng) {
            const flag = L.icon({
                iconUrl: '../assets/Stanford_Logo.png',
                iconSize: [80, 35]
            });
            return L.marker(latlng, {
                icon: flag
            });
        },
        function2: function(e, ctx) {
            ctx.setProps({
                latlng_data: e.latlng
            })
        }
    }
});