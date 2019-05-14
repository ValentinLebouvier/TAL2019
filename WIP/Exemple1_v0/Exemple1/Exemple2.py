import py_trees
import time

class Action(py_trees.behaviour.Behaviour):
    
    def __init__(self, name="Action"):
        super(Action, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))
    
    def setup(self):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))\
    
    def initialise(self):
        self.logger.debug("%s.initialise()" % (self.__class__.__name__))
        self.startTimer = time.time()
        self.endExec = 5
        
    def update(self):
        new_status = py_trees.common.Status.RUNNING
        t = time.time();
        
        if (t-self.startTimer>=self.endExec):
            new_status = py_trees.common.Status.SUCCESS
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__,self.status, new_status, self.feedback_message))
        return new_status
    
    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s][%s]" % (self.__class__.__name__,self.status, new_status, self.feedback_message))
        
        
        
class Condition(py_trees.behaviour.Behaviour):
    
    def __init__(self, name="Action"):
        super(Action, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))
    
    def setup(self):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
    
    def initialise(self):
        self.logger.debug("%s.initialise()" % (self.__class__.__name__))
        self.startTimer = time.time()
        self.endExec = 5
        
    def update(self):
        new_status = py_trees.common.Status.RUNNING
        
        if ():
            new_status = py_trees.common.Status.SUCCESS
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__,self.status, new_status, self.feedback_message))
        return new_status
    
    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s][%s]" % (self.__class__.__name__,self.status, new_status, self.feedback_message))
    
        
        

def create_root():
    
    root = py_trees.composites.Sequence("Sequence")
    fallback1 = py_trees.composites.Selector("Selector1")
    fallback2 = py_trees.composites.Selector("Selector2")
    fallback3 = py_trees.composites.Selector("Selector3")
    
    
    goto_block = Action("Goto_Block")
    grab_block = Action("Grab_Block")
    goto_goal = Action("Goto_Goal")
    place_goal = Action("Place_Goal")
    root.add_children([fallback1,fallback2,fallback3,place_goal])
    return root




if __name__ == "__main__":
    py_trees.logging.level = py_trees.logging.Level.DEBUG
    
    root = create_root()
    
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)
    
    try:
        tree.tick_tock(
            500,
            py_trees.trees.CONTINUOUS_TICK_TOCK,
            None,
            None
        )
    except KeyboardInterrupt:
        tree.interrupt()