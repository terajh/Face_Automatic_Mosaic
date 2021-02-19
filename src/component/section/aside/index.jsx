import React from 'react';
import { Nav } from "react-bootstrap";
import './style.css';
// eslint-disable-next-line

const Aside = () => {
    return (
        <div className="span4">
            <div id="toolbar" className="well">
                <form className="form-in">
                    <div className="control-group">
                        <legend>Mozaic Control</legend>

                    </div>

                    <div className="control-group">
                        <div id="manualSelectionControlGroup">

                            <label className="labels" style={{ "justifyContent": "end" }}>Size</label>
                            <div className="slidecontainer">
                                <input type="range" min="1" max="100" className="slider" id="myRange" />
                            </div>
                            
                            <div className="controls">
                                <label className="labels" style={{ "justifyContent": "end" }}>Preview</label>
                                <br />
                                <canvas id="previewCanvas" width="270" height="270"></canvas>
                            </div>
                        </div>
                    </div>
                    <div className="control-group">
                        <legend>Save</legend>
                        <div className="controls">
                            <button id="down_images" className="btn btn-success" type="button" >Save Image</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    );
}
export default Aside;