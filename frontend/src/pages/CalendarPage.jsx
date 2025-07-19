// frontend/src/pages/CalendarPage.jsx
import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';

const CalendarPage = () => {
  const [events, setEvents] = useState([]);

  const handleDateSelect = (selectInfo) => {
    const title = prompt('Enter session title:');
    if (title) {
      setEvents([
        ...events,
        {
          title,
          start: selectInfo.startStr,
          end: selectInfo.endStr,
          allDay: false
        }
      ]);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Scheduler Calendar</h1>
      <FullCalendar
        plugins={[timeGridPlugin, interactionPlugin]}
        initialView="timeGridWeek"
        selectable={true}
        select={handleDateSelect}
        events={events}
        height="auto"
      />
    </div>
  );
};

export default CalendarPage;
