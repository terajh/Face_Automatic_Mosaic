import React, { useState, useEffect } from 'react';
import './style.css';
const Content = () => {
    // eslint-disable-next-line
    const [url, seturl] = useState(0);
    useEffect(() => {
    })
    return (
        <div className="well" id="img_upload">
            <div className="img_upload">
                <input type="file" id="real-input" className="input-btn" accept="img/*" required multiple />
                <button className="browse-btn" style={{display:'none'}}>Image Upload</button>
            </div>

            <canvas id="jsCanvas" className="canvas" width="1080" height="730"></canvas>
        </div>
    )
}

export default Content;