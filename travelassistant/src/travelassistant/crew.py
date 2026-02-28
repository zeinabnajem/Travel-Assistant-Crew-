from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import random
import datetime
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Travelassistant():
    """Travelassistant crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def flight_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_agent'], # type: ignore[index]
            verbose=True
        )
    @agent
    def hotel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['hotel_agent'], # type: ignore[index]
            verbose=True
        )    

    @agent
    def tour_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tour_agent'], # type: ignore[index]
            verbose=True
        )    

    @agent
    def advisor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['advisor_agent'], # type: ignore[index]
            verbose=True
        )    
   
        
        

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def flight_booking_task(self) -> Task:
        # Dummy function to generate flights
        def dummy_flights(destination):
            airlines = ["Delta", "Emirates", "Qatar Airways", "Turkish Airlines", "Lufthansa"]
            flights = []
            for _ in range(5):
                flight = {
                    "airline": random.choice(airlines),
                    "departure": f"{random.randint(1,28)}/03/2026 {random.randint(0,23)}:{random.choice(['00','30'])}",
                    "arrival": f"{random.randint(1,28)}/03/2026 {random.randint(0,23)}:{random.choice(['00','30'])}",
                    "price": f"${random.randint(200,1200)}"
                }
                flights.append(flight)
            return flights

        return Task(
            config=self.tasks_config['flight_booking_task'],  # type: ignore[index]
            func=dummy_flights
        )
    @task
    def hotel_booking_task(self) -> Task:
        def dummy_hotels(destination):
            hotel_names = ["Grand Hotel", "Sunset Inn", "Ocean View Resort", "City Center Lodge", "Luxury Suites"]
            hotels = []
            for _ in range(5):
                hotel = {
                    "name": random.choice(hotel_names),
                    "location": destination,
                    "amenities": random.sample(["WiFi","Pool","Breakfast","Gym","Spa"], 3),
                    "price": f"${random.randint(50,500)} per night"
                }
                hotels.append(hotel)
            return hotels

        return Task(
            config=self.tasks_config['hotel_booking_task'],  # type: ignore[index]
            func=dummy_hotels
        )

    @task
    def tour_booking_task(self) -> Task:
        def dummy_tours(destination):
            tour_names = ["City Highlights Tour", "Food & Culture Tour", "Historic Sites Tour", "Adventure Trek", "Relaxing Beach Tour"]
            tours = []
            for _ in range(5):
                tour = {
                    "name": random.choice(tour_names),
                    "location": destination,
                    "duration": f"{random.randint(2,8)} hours",
                    "price": f"${random.randint(30,150)}"
                }
                tours.append(tour)
            return tours

        return Task(
            config=self.tasks_config['tour_booking_task'],  # type: ignore[index]
            func=dummy_tours
        )

    @task
    def advice_task(self) -> Task:
        def travel_advice(destination):
            advice_list = [
                f"Check local weather before visiting {destination}.",
                f"Learn a few basic phrases in the local language of {destination}.",
                f"Try the local cuisine in {destination} for an authentic experience.",
                f"Always carry a map or offline GPS when exploring {destination}.",
                f"Respect local customs and traditions in {destination}.",
            ]
            return advice_list

        return Task(
            config=self.tasks_config['advice_task'],  # type: ignore[index]
            func=travel_advice
        )
    

    

    @crew
    def crew(self) -> Crew:
        """Creates the Travelassistant crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
