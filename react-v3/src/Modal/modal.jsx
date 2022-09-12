import React from 'react';
import "./modal.css";

const Modal = ({active, SetActive}) => {
    return (
        <div className={active ? "modal69 active" : "modal69"} onClick={() => SetActive(false)}>
            <div className="content69" onClick={tmp => tmp.stopPropagation()}>

            </div>

        </div>
    )
}

export default Modal;