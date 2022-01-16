import React, { Component } from 'react';

class App extends Component {
    state = {
        messages: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const messages = await res.json();
            this.setState({
                messages
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div>
                {this.state.messages.map(item => (
                    <div>
                        <h1>{item.send_text}</h1>
                        <p>{item.pub_date}</p>    
                        <p>{item.check_read}</p>
                        <p>{item.check_user}</p>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;