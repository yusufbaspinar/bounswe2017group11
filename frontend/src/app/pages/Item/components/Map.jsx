import React from "react"
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"
import PropTypes from 'prop-types';

/**
 *	Component for showing location of an item on Google Maps
 *
 *	Makes use of the library react-google-maps
 *
 *	Gets item location in latitud and longtitude. Passes the location to the GoogleMap component.
 */
export default class ItemMap extends React.PureComponent {
	static propTypes = {
         /** Location object of the item */
         location: PropTypes.object,
         /** Key of the location object */
         key: PropTypes.bool
    }
	constructor(props){
		super(props)
		this.state = {
      		position:{
          		lat: this.props.location.latitude,
          		lng: this.props.location.longtitude,
        	}
    	}
    	console.log(this.state.position)
	}

  	render() {
  		var lng = parseFloat(this.state.position.lng)
  		var lat = parseFloat(this.state.position.lat)
  		const MyMapComponent = compose(
		 	withProps({
		    	googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&key=AIzaSyBB--q2zvaQhc7FJL5gjhcliMleltyAmDs&libraries=geometry,drawing,places",
		    	loadingElement: <div style={{ height: `100%` }} />,
		    	containerElement: <div style={{ height: `400px` }} />,
		    	mapElement: <div style={{ height: `100%` }} />,
		  	}),
		  	withScriptjs,
		  	withGoogleMap
			)((props) =>
		  		<GoogleMap
		    		defaultZoom={8}
		    		defaultCenter={{lat: lat, lng: lng}}
		  		>
		  		{console.log(this.state.position)}
		    		{props.isMarkerShown && <Marker position={{lat: lat, lng: lng}} />}
		  		
		  		</GoogleMap>,
			)
    	return (
     	 <MyMapComponent
        	isMarkerShown={true}
     	 />
    	)
  	}
}