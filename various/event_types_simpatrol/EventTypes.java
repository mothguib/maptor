/* EventTypes.java */

/* The package of this class. */
package control.event;

/**
 * Holds the types of events handled by SimPatrol.
 * 
 * @see Event
 * @developer New event types must be added here.
 */
public abstract class EventTypes {
	/**
	 * The events related to to creation of an agent.
	 * 
	 * @see
	 */
	public static final int AGENT_CREATION = 0;

	/**
	 * The events related to to the death of an agent.
	 * 
	 * @see AgentDeathEvent
	 */
	public static final int AGENT_DEATH = 1;

	/**
	 * The events related to the changing of state of the agents.
	 * 
	 * @see AgentChangingStateEvent
	 */
	public static final int AGENT_CHANGING_STATE = 2;

	/**
	 * The events related to the spending of stamina of the agents.
	 * 
	 * @see AgentSpendingStaminaEvent
	 */
	public static final int AGENT_SPENDING_STAMINA = 3;

	/**
	 * The events related to the recharging of the agents.
	 * 
	 * @see AgentRechargingEvent
	 */
	public static final int AGENT_RECHARGING = 4;

	/**
	 * The events related to the teleporting of the agents.
	 * 
	 * @see AgentTeleportingEvent
	 */
	public static final int AGENT_TELEPORTING = 5;

	/**
	 * The events related to the agents visiting the nodes.
	 * 
	 * @see AgentVisitEvent
	 */
	public static final int AGENT_VISIT = 6;

	/**
	 * The events related to the agents depositing stigmas on the graph.
	 * 
	 * @see AgentStigmatizingEvent
	 */
	public static final int AGENT_STIGMATIZING = 7;

	/**
	 * The events related to the agents broadcasting messages through the graph.
	 * 
	 * @see AgentBroadcastingEvent
	 */
	public static final int AGENT_BROADCASTING = 8;

	/**
	 * The events related to the agents receiving messages on the graph.
	 * 
	 * @see AgentReceivingMessageEvent
	 */
	public static final int AGENT_RECEIVING_MESSAGE = 9;

	/**
	 * The events related to the enabling / disabling of dynamic nodes.
	 * 
	 * @see NodeEnablingEvent
	 */
	public static final int NODE_ENABLING = 10;

	/**
	 * The events related to the enabling / disabling of edges.
	 * 
	 * @see EdgeEnablingEvent
	 */
	public static final int EDGE_ENABLING = 11;
	
	
	
	/**
	 * The events related to the activation of agents.
	 * 
	 * @see AgentActivatingEvent
	 */
	public static final int AGENT_ACTIVATING = 12;
	
	/**
	 * The events related to the deactivation of agents.
	 * 
	 * @see AgentDeactivatingEvent
	 */
	public static final int AGENT_DEACTIVATING = 13;
	
	/**
	 * The events related to the changing of society of agents.
	 * 
	 * @see AgentChangingSocietyEvent
	 */
	public static final int AGENT_CHANGING_SOCIETY = 14;
	
	
	
	/**
	 * The events related to the agent sending a message.
	 * 
	 * @see AgentSendingMessageEvent
	 */
	public static final int AGENT_SENDING_MESSAGE = 15;	
	
	
	
}
