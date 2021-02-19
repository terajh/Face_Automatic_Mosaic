import React from 'react';
import './style.css'
import Content from './content';
import Aside from './aside';
import Detail from './detail';

import { Container, Row, Col } from "react-bootstrap";
const Section = () => {
    return (
        <div className="main_body">
            <div className='rows' >
                <Aside></Aside>

                <Content />
                <Detail></Detail>
                <div className="modal"></div>
            </div>
        </div>
    )
}
export default Section;