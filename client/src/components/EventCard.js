import React, { useState, useEffect } from "react";

function EventCard() {
    const [userData, setUserData] = useState(null);
    const [events, setEvents] = useState([]);
    const [tasks, setTasks] = useState([]);

    const activeUser = sessionStorage.getItem('userId');
    const activeToken = sessionStorage.getItem('accessToken');
    console.log(activeUser);
    console.log(activeToken);

    useEffect(() => {
        async function fetchData() {
            try {
                // Fetch user data
                const userResponse = await fetch(`/users/${activeUser}`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${activeToken}`
                    }
                });
                if (!userResponse.ok) {
                    throw new Error("Failed to fetch user data");
                }
                const userData = await userResponse.json();
                setUserData(userData);

                // Fetch events
                const eventsResponse = await fetch('/events', {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${activeToken}`
                    }
                });
                if (!eventsResponse.ok) {
                    throw new Error("Failed to fetch events");
                }
                const eventsData = await eventsResponse.json();
                setEvents(eventsData);

                //Fetch tasks
                const tasksResponse = await fetch(`/tasks`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${activeToken}`
                    }
                });
                if (!tasksResponse.ok) {
                    throw new Error("Failed to fetch tasks");
                }
                const tasksData = await tasksResponse.json();
                setTasks(tasksData);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }
        fetchData();
    }, [activeUser, activeToken]); 

    return (
        <>
            {userData && userData.title === "planner" ? (
                <div>
                    <p>Name: {userData.first_name} {userData.last_name}</p>
                    <p>Email: {userData.email}</p>
                    <h2>Events:</h2>
                    {events.map(event => (
                        <div key={event.id}>
                            <ul>Title: {event.title}</ul>
                            {event.tasks ? (
                                <ul>
                                    {event.tasks.map(task => (
                                        <li key={task.id}>Task title; {task.title}</li>
                                    ))}
                                </ul>
                            ) : (
                                <p>No tasks available</p>
                            )}
                            <p>Start Date: {event.start_date}</p>
                            <p>End Date: {event.end_date}</p>
                            {/* Add other event details as needed */}
                        </div>
                    ))}
                </div>
            ) : (
                <p>Loading user data...</p>
            )}
        </>
    );
}

export default EventCard;

